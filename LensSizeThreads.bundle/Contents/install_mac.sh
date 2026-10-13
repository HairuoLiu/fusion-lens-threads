#!/usr/bin/env bash
#
# install_mac.sh  —  Install "Camera Lens and Filter Threads" into Autodesk Fusion 360 (macOS)
#
# What it does:
#   1. Auto-detects ALL Fusion 360 ThreadData folders (every webdeploy version
#      build on this machine).
#   2. Generates two thread families:
#        LensSizeThreads.xml  - all common lens/filter diameters 24..127 mm with
#                               both 0.75 mm and 1.0 mm pitch, plus the special
#                               Leica Thread Mount pitch on 39 mm
#                               (M39 x 1/26" = 26 TPI = 0.976923 mm).
#        LensMountThreads.xml - the same L39 / LTM mount with the historically
#                               correct Whitworth 55 degree flank angle.
#   3. Copies both files into EVERY detected folder. Restart Fusion afterwards.
#
# Usage:
#   ./install_mac.sh                 # auto-detect & install
#   ./install_mac.sh --dry-run      # only print the detected paths
#   ./install_mac.sh --output DIR   # write into DIR instead (manual install / testing)
#
# Requires: bash 3+ (no Python needed). Works on macOS.
#
set -euo pipefail

# ---------------------------------------------------------------------------
# Configuration (mirrors generate_lens_threads.py)
# ---------------------------------------------------------------------------
FAMILY_NAME="Camera Lens and Filter Threads"
UNIT="mm"
ANGLE="60"
SORT_ORDER="100"
ALLOWANCE="0.10"

SIZES=(24 25 25.5 27 28 30 30.5 34 35.5 36 36.5 37 37.5 38.5 39 40
        40.5 41 42 43 43.5 44 46 46.5 48 49 50 50.5 52 54 55 56 58 60
        62 64 67 70 72 74 75 76 77 78 80 82 84 85 86 87 90 92 94 95 96
        98 100 102 104 105 107 108 110 112 114 116 118 120 122 124 125 126 127)
PITCHES=(0.75 1.0)

# --- Special (non-metric) mount threads -------------------------------------
# Leica Thread Mount (L39 / LTM / LSM): 39 mm, 26 threads per inch.
# Pitch = 25.4 mm / 26 = 0.976923 mm (NOT 1.0 mm, NOT 0.75 mm).
LTM_PITCH=$(awk 'BEGIN{printf "%.15f", 25.4/26}')
SPECIAL_SIZES=(39)
SPECIAL_LABELS=("L39x1/26-LTM")
SPECIAL_PITCHES=("$LTM_PITCH")

# Second family: correct Whitworth 55 degree flank angle for the L39 mount.
LTM_FAMILY_NAME="Leica Thread Mount (L39/LTM)"
LTM_ANGLE="55"
LTM_SORT_ORDER="101"
LTM_SIZES=(39)
LTM_LABELS=("L39x1/26")
LTM_PITCHES=("$LTM_PITCH")
WHITWORTH_DEPTH="0.640327"

OUTPUT_OVERRIDE=""
DRY_RUN=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --output) OUTPUT_OVERRIDE="$2"; shift 2;;
    --dry-run) DRY_RUN=1; shift;;
    -h|--help)
      grep '^#' "$0" | sed 's/^# \{0,1\}//'; exit 0;;
    *) echo "Unknown argument: $1" >&2; exit 1;;
  esac
done

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
fmt() {
  # integer -> "N", else up to 4 decimals with trailing zeros stripped
  awk -v x="$1" 'BEGIN{
    if (x == int(x)) { printf "%d", int(x + 0.5) }
    else { s = sprintf("%.4f", x); sub(/0+$/, "", s); sub(/\.$/, "", s); printf "%s", s }
  }'
}

fmt_p() {
  # pitch: up to 6 decimals (26 TPI = 0.976923 needs more than 4)
  awk -v x="$1" 'BEGIN{
    if (x == int(x)) { printf "%d", int(x + 0.5) }
    else { s = sprintf("%.6f", x); sub(/0+$/, "", s); sub(/\.$/, "", s); printf "%s", s }
  }'
}

compute() {
  # $1 nominal $2 pitch $3 sign(-1 external / +1 internal)  -> ISO metric 60 deg
  # prints "major pitch minor"
  awk -v n="$1" -v p="$2" -v s="$3" -v k="$ALLOWANCE" 'BEGIN{
    H  = 0.8660254037844386 * p;
    pb = n - 0.75 * H;
    mb = n - 1.25 * H;
    printf "%.6f %.6f %.6f", n + s*k, pb + s*k, mb + s*k;
  }'
}

compute_whitworth() {
  # $1 nominal $2 pitch $3 sign(-1 external / +1 internal) -> Whitworth 55 deg
  awk -v n="$1" -v p="$2" -v s="$3" -v k="$ALLOWANCE" -v w="$WHITWORTH_DEPTH" 'BEGIN{
    d  = w * p;
    pb = n - d;
    mb = n - 2.0 * d;
    printf "%.6f %.6f %.6f", n + s*k, pb + s*k, mb + s*k;
  }'
}

add_designation() {
  # $1 label  $2 pitch  $3 external dims  $4 internal dims
  local label="$1" p="$2"
  local em ep emi im ip imi
  read em ep emi <<< "$3"
  read im ip imi <<< "$4"

  echo "    <Designation>"
  echo "      <ThreadDesignation>$label</ThreadDesignation>"
  echo "      <CTD>$label</CTD>"
  echo "      <Pitch>$(fmt_p "$p")</Pitch>"

  echo "      <Thread>"
  echo "        <Gender>external</Gender>"
  echo "        <Class>6g</Class>"
  echo "        <MajorDia>$(fmt "$em")</MajorDia>"
  echo "        <PitchDia>$(fmt "$ep")</PitchDia>"
  echo "        <MinorDia>$(fmt "$emi")</MinorDia>"
  echo "      </Thread>"

  echo "      <Thread>"
  echo "        <Gender>internal</Gender>"
  echo "        <Class>6H</Class>"
  echo "        <MajorDia>$(fmt "$im")</MajorDia>"
  echo "        <PitchDia>$(fmt "$ip")</PitchDia>"
  echo "        <MinorDia>$(fmt "$imi")</MinorDia>"
  echo "      </Thread>"

  echo "    </Designation>"
}

build_xml() {
  echo '<?xml version="1.0" encoding="UTF-8"?>'
  echo "<ThreadType>"
  echo "  <Name>$FAMILY_NAME</Name>"
  echo "  <CustomName>$FAMILY_NAME</CustomName>"
  echo "  <Unit>$UNIT</Unit>"
  echo "  <Angle>$ANGLE</Angle>"
  echo "  <SortOrder>$SORT_ORDER</SortOrder>"

  local i
  for size in "${SIZES[@]}"; do
    fs=$(fmt "$size")
    echo "  <ThreadSize>"
    echo "    <Size>$fs</Size>"
    for pitch in "${PITCHES[@]}"; do
      design="M${fs}x$(fmt_p "$pitch")"
      add_designation "$design" "$pitch" \
        "$(compute "$size" "$pitch" -1)" \
        "$(compute "$size" "$pitch" 1)"
    done
    # Special (non-metric) designations for this size, e.g. L39 / LTM 26 TPI
    for ((i = 0; i < ${#SPECIAL_SIZES[@]}; i++)); do
      if awk -v a="$size" -v b="${SPECIAL_SIZES[$i]}" 'BEGIN{exit !(a == b)}'; then
        add_designation "${SPECIAL_LABELS[$i]}" "${SPECIAL_PITCHES[$i]}" \
          "$(compute "$size" "${SPECIAL_PITCHES[$i]}" -1)" \
          "$(compute "$size" "${SPECIAL_PITCHES[$i]}" 1)"
      fi
    done
    echo "  </ThreadSize>"
  done
  echo "</ThreadType>"
}

build_ltm_xml() {
  echo '<?xml version="1.0" encoding="UTF-8"?>'
  echo "<ThreadType>"
  echo "  <Name>$LTM_FAMILY_NAME</Name>"
  echo "  <CustomName>$LTM_FAMILY_NAME</CustomName>"
  echo "  <Unit>$UNIT</Unit>"
  echo "  <Angle>$LTM_ANGLE</Angle>"
  echo "  <SortOrder>$LTM_SORT_ORDER</SortOrder>"

  local i
  for ((i = 0; i < ${#LTM_SIZES[@]}; i++)); do
    echo "  <ThreadSize>"
    echo "    <Size>$(fmt "${LTM_SIZES[$i]}")</Size>"
    add_designation "${LTM_LABELS[$i]}" "${LTM_PITCHES[$i]}" \
      "$(compute_whitworth "${LTM_SIZES[$i]}" "${LTM_PITCHES[$i]}" -1)" \
      "$(compute_whitworth "${LTM_SIZES[$i]}" "${LTM_PITCHES[$i]}" 1)"
    echo "  </ThreadSize>"
  done
  echo "</ThreadType>"
}

find_all_mac_paths() {
  local base="$HOME/Library/Application Support/Autodesk/Webdeploy/production"
  [ -d "$base" ] || return 0
  local vdirs
  vdirs=$(find "$base" -maxdepth 1 -mindepth 1 -type d 2>/dev/null)
  local results=""
  for vdir in $vdirs; do
    local cand=(
      "$vdir/Autodesk Fusion 360.app/Contents/Libraries/Applications/Fusion/Fusion/Server/Fusion/Configuration/ThreadData"
      "$vdir/Autodesk Fusion 360.app/Contents/Libraries/Applications/Fusion/Server/fusion/Configuration/ThreadData"
    )
    local c
    for c in "${cand[@]}"; do
      [ -d "$c" ] && results="${results}${c}"$'\n'
    done
  done
  printf '%s' "$results"
}

write_files() {
  # $1 destination directory
  local dir="$1"
  build_xml > "$dir/LensSizeThreads.xml"
  build_ltm_xml > "$dir/LensMountThreads.xml"
  echo "  $dir/LensSizeThreads.xml"
  echo "  $dir/LensMountThreads.xml"
}

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
if [ -n "$OUTPUT_OVERRIDE" ]; then
  DEST_DIR="$OUTPUT_OVERRIDE"
  mkdir -p "$DEST_DIR"
  echo "Wrote:"
  write_files "$DEST_DIR"
  echo "Restart Fusion 360, then look for thread types:"
  echo "  $FAMILY_NAME"
  echo "  $LTM_FAMILY_NAME"
  exit 0
fi

MAC_PATHS=$(find_all_mac_paths)
if [ -z "$MAC_PATHS" ]; then
  echo "ERROR: Could not auto-detect the Fusion 360 ThreadData folder." >&2
  echo "Run with --output /path/to/ThreadData to install manually," >&2
  echo "or check the path at:" >&2
  echo "  ~/Library/Application Support/Autodesk/Webdeploy/production/<version>/Autodesk Fusion 360.app/Contents/Libraries/Applications/Fusion/Fusion/Server/Fusion/Configuration/ThreadData" >&2
  exit 1
fi

if [ "$DRY_RUN" = 1 ]; then
  echo "$MAC_PATHS" | while IFS= read -r p; do
    [ -n "$p" ] && echo "[dry-run] would install to: $p"
  done
  exit 0
fi

echo "$MAC_PATHS" | while IFS= read -r p; do
  [ -z "$p" ] && continue
  echo "Installed to:"
  write_files "$p"
done
echo "Restart Fusion 360, then look for thread types:"
echo "  $FAMILY_NAME"
echo "  $LTM_FAMILY_NAME"
