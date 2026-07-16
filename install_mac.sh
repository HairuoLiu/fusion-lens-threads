#!/usr/bin/env bash
#
# install_mac.sh  —  Install "Camera Lens and Filter Threads" into Autodesk Fusion 360 (macOS)
#
# What it does:
#   1. Auto-detects ALL Fusion 360 ThreadData folders (every webdeploy version
#      build on this machine).
#   2. Generates LensSizeThreads.xml (all common lens/filter diameters 24..127 mm,
#      with both 0.75 mm and 1.0 mm pitch).
#   3. Copies the file into EVERY detected folder. Restart Fusion 360 afterwards.
#
# Usage:
#   ./install_mac.sh                 # auto-detect & install
#   ./install_mac.sh --dry-run      # only print the detected path
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

compute() {
  # $1 nominal $2 pitch $3 sign(-1 external / +1 internal)
  # prints "major pitch minor"
  awk -v n="$1" -v p="$2" -v s="$3" -v k="$ALLOWANCE" 'BEGIN{
    H  = 0.8660254037844386 * p;
    pb = n - 0.75 * H;
    mb = n - 1.25 * H;
    printf "%.4f %.4f %.4f", n + s*k, pb + s*k, mb + s*k;
  }'
}

build_xml() {
  echo '<?xml version="1.0" encoding="UTF-8"?>'
  echo "<ThreadType>"
  echo "  <Name>$FAMILY_NAME</Name>"
  echo "  <CustomName>$FAMILY_NAME</CustomName>"
  echo "  <Unit>$UNIT</Unit>"
  echo "  <Angle>$ANGLE</Angle>"
  echo "  <SortOrder>$SORT_ORDER</SortOrder>"

  for size in "${SIZES[@]}"; do
    fs=$(fmt "$size")
    echo "  <ThreadSize>"
    echo "    <Size>$fs</Size>"
    for pitch in "${PITCHES[@]}"; do
      fp=$(fmt "$pitch")
      design="M${fs}x${fp}"
      echo "    <Designation>"
      echo "      <ThreadDesignation>$design</ThreadDesignation>"
      echo "      <CTD>$design</CTD>"
      echo "      <Pitch>$fp</Pitch>"

      dims=$(compute "$size" "$pitch" -1)
      read em ep emi <<< "$dims"
      echo "      <Thread>"
      echo "        <Gender>external</Gender>"
      echo "        <Class>6g</Class>"
      echo "        <MajorDia>$(fmt "$em")</MajorDia>"
      echo "        <PitchDia>$(fmt "$ep")</PitchDia>"
      echo "        <MinorDia>$(fmt "$emi")</MinorDia>"
      echo "      </Thread>"

      dims=$(compute "$size" "$pitch" 1)
      read im ip imi <<< "$dims"
      echo "      <Thread>"
      echo "        <Gender>internal</Gender>"
      echo "        <Class>6H</Class>"
      echo "        <MajorDia>$(fmt "$im")</MajorDia>"
      echo "        <PitchDia>$(fmt "$ip")</PitchDia>"
      echo "        <MinorDia>$(fmt "$imi")</MinorDia>"
      echo "      </Thread>"

      echo "    </Designation>"
    done
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

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
if [ -n "$OUTPUT_OVERRIDE" ]; then
  DEST_DIR="$OUTPUT_OVERRIDE"
  mkdir -p "$DEST_DIR"
  build_xml > "$DEST_DIR/LensSizeThreads.xml"
  echo "Wrote: $DEST_DIR/LensSizeThreads.xml"
  echo "Restart Fusion 360, then look for thread type: $FAMILY_NAME"
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
  build_xml > "$p/LensSizeThreads.xml"
  echo "Installed LensSizeThreads.xml to:"
  echo "  $p"
done
echo "Restart Fusion 360, then look for thread type: $FAMILY_NAME"
