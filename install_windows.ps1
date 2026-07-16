<#
  install_windows.ps1  -  Install "镜头尺寸螺纹规格" lens threads into Autodesk Fusion 360 (Windows)

  What it does:
    1. Auto-detects the Fusion 360 ThreadData folder (newest webdeploy version).
    2. Generates LensSizeThreads.xml (all common lens/filter diameters 24..127 mm,
       with both 0.75 mm and 1.0 mm pitch).
    3. Copies the file into the detected folder. Restart Fusion 360 afterwards.

  Usage:
    powershell -ExecutionPolicy Bypass -File install_windows.ps1
    powershell -ExecutionPolicy Bypass -File install_windows.ps1 -WhatIf      # only print the detected path
    powershell -ExecutionPolicy Bypass -File install_windows.ps1 -OutputDir DIR  # manual install / testing

  Requires: Windows PowerShell 5.1+ (no Python needed).
#>

[CmdletBinding()]
param(
  [string]$OutputDir = "",
  [switch]$WhatIf
)

# ---------------------------------------------------------------------------
# Configuration (mirrors generate_lens_threads.py)
# ---------------------------------------------------------------------------
# Family name shown in Fusion 360's "Thread Type" dropdown.
# Written as \u escapes (pure ASCII source) so the .ps1 file decodes
# correctly on any Windows codepage (avoids garbled Chinese).
$FAMILY_NAME = [regex]::Unescape("\u955c\u5934\u5c3a\u5bf8\u87ba\u7eb9\u89c4\u683c")
$UNIT        = "mm"
$ANGLE       = "60"
$SORT_ORDER  = "100"
$ALLOWANCE   = 0.10

$SIZES = @(24, 25, 25.5, 27, 28, 30, 30.5, 34, 35.5, 36, 36.5, 37, 37.5,
            38.5, 39, 40, 40.5, 41, 42, 43, 43.5, 44, 46, 46.5, 48, 49, 50,
            50.5, 52, 54, 55, 56, 58, 60, 62, 64, 67, 70, 72, 74, 75, 76, 77,
            78, 80, 82, 84, 85, 86, 87, 90, 92, 94, 95, 96, 98, 100, 102, 104,
            105, 107, 108, 110, 112, 114, 116, 118, 120, 122, 124, 125, 126, 127)
$PITCHES = @(0.75, 1.0)

$sqrt32 = [math]::Sqrt(3) / 2

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
function fmt($x) {
  if ([math]::Abs($x - [math]::Round($x)) -lt 1e-9) {
    return [int][math]::Round($x)
  }
  return ('{0:0.####}' -f $x).TrimEnd('0').TrimEnd('.')
}

function Compute($nominal, $pitch, $gender) {
  $H  = $sqrt32 * $pitch
  $pb = $nominal - 0.75 * $H
  $mb = $nominal - 1.25 * $H
  # derive sign from gender (avoids the "-1 as switch" PowerShell pitfall)
  $sign = if ($gender -eq 'external') { -1.0 } else { 1.0 }
  $major  = $nominal + $sign * $ALLOWANCE
  $pitchD = $pb + $sign * $ALLOWANCE
  $minorD = $mb + $sign * $ALLOWANCE
  return @($major, $pitchD, $minorD)
}

function Build-Xml {
  $lines = [System.Collections.Generic.List[string]]::new()
  $lines.Add('<?xml version="1.0" encoding="UTF-8"?>')
  $lines.Add("<ThreadType>")
  $lines.Add("  <Name>$FAMILY_NAME</Name>")
  $lines.Add("  <CustomName>$FAMILY_NAME</CustomName>")
  $lines.Add("  <Unit>$UNIT</Unit>")
  $lines.Add("  <Angle>$ANGLE</Angle>")
  $lines.Add("  <SortOrder>$SORT_ORDER</SortOrder>")

  foreach ($size in $SIZES) {
    $fs = fmt $size
    $lines.Add("  <ThreadSize>")
    $lines.Add("    <Size>$fs</Size>")
    foreach ($pitch in $PITCHES) {
      $fp = fmt $pitch
      $design = "M${fs}x${fp}"
      $lines.Add("    <Designation>")
      $lines.Add("      <ThreadDesignation>$design</ThreadDesignation>")
      $lines.Add("      <CTD>$design</CTD>")
      $lines.Add("      <Pitch>$fp</Pitch>")

      $e = Compute $size $pitch 'external'
      $lines.Add("      <Thread>")
      $lines.Add("        <Gender>external</Gender>")
      $lines.Add("        <Class>6g</Class>")
      $lines.Add("        <MajorDia>$(fmt $e[0])</MajorDia>")
      $lines.Add("        <PitchDia>$(fmt $e[1])</PitchDia>")
      $lines.Add("        <MinorDia>$(fmt $e[2])</MinorDia>")
      $lines.Add("      </Thread>")

      $i = Compute $size $pitch 'internal'
      $lines.Add("      <Thread>")
      $lines.Add("        <Gender>internal</Gender>")
      $lines.Add("        <Class>6H</Class>")
      $lines.Add("        <MajorDia>$(fmt $i[0])</MajorDia>")
      $lines.Add("        <PitchDia>$(fmt $i[1])</PitchDia>")
      $lines.Add("        <MinorDia>$(fmt $i[2])</MinorDia>")
      $lines.Add("      </Thread>")

      $lines.Add("    </Designation>")
    }
    $lines.Add("  </ThreadSize>")
  }
  $lines.Add("</ThreadType>")
  return $lines -join "`n"
}

function Detect-WindowsPath {
  $bases = @(
    Join-Path $env:LOCALAPPDATA "Autodesk\webdeploy\Production",
    Join-Path $env:LOCALAPPDATA "Autodesk\webdeploy\production"
  )
  foreach ($base in $bases) {
    if (-not (Test-Path $base)) { continue }
    $verDirs = Get-ChildItem $base -Directory | Sort-Object LastWriteTime -Descending
    foreach ($v in $verDirs) {
      $cands = @(
        Join-Path $v.FullName "Fusion\Server\fusion\Configuration\ThreadData",
        Join-Path $v.FullName "Fusion\Server\Fusion\Configuration\ThreadData"
      )
      foreach ($c in $cands) {
        if (Test-Path $c) { return $c }
      }
    }
  }
  return $null
}

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
if ($OutputDir -ne "") {
  New-Item -ItemType Directory -Force -Path $OutputDir | Out-Null
  $dest = Join-Path $OutputDir "LensSizeThreads.xml"
  # UTF-8 WITHOUT BOM (matches the Python / bash generators)
  [System.IO.File]::WriteAllText($dest, (Build-Xml), [System.Text.UTF8Encoding]::new($false))
  Write-Host "Wrote: $dest"
  Write-Host "Restart Fusion 360, then look for thread type: $FAMILY_NAME"
  exit 0
}

$winPath = Detect-WindowsPath
if ($winPath) {
  if ($WhatIf) {
    Write-Host "[WhatIf] would install to: $winPath"
    exit 0
  }
  $dest = Join-Path $winPath "LensSizeThreads.xml"
  [System.IO.File]::WriteAllText($dest, (Build-Xml), [System.Text.UTF8Encoding]::new($false))
  Write-Host "Installed LensSizeThreads.xml to:"
  Write-Host "  $dest"
  Write-Host "Restart Fusion 360, then look for thread type: $FAMILY_NAME"
  exit 0
}

Write-Error "Could not auto-detect the Fusion 360 ThreadData folder."
Write-Host "Run with -OutputDir <path-to-ThreadData> to install manually, e.g.:" -ForegroundColor Yellow
Write-Host "  %LOCALAPPDATA%\Autodesk\webdeploy\Production\<version>\Fusion\Server\fusion\Configuration\ThreadData" -ForegroundColor Yellow
exit 1
