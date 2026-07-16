# Fusion 360 Lens Size Thread Specs — v1.0.0

First stable release. A zero-dependency, cross-platform way to add **lens & filter thread sizes** (M24–M127) directly into Autodesk Fusion 360's built-in Thread tool.

## What's included
- **73 lens/filter diameters** (24–127 mm) — covers the common 39, 40, 42, 43 mm sizes and many more.
- **Two pitches per size**: `0.75 mm` (filter threads) and `1.0 mm` (e.g. M42×1 mount), so lenses and step-up rings actually screw in.
- **External (bolt) + internal (hole)** threads for every size, with correct 6g/6H clearance.
- One new thread family in Fusion: **"镜头尺寸螺纹规格" (Lens Size Threads)**.

## Install in ~30 seconds
1. **macOS**: `bash install_mac.sh`
2. **Windows (PowerShell)**: `.\install_windows.ps1`
3. Restart Fusion 360 → *Create › Thread* → pick **镜头尺寸螺纹规格**.

Both installers auto-detect Fusion's `ThreadData` folder (newest version) and drop `LensSizeThreads.xml` there. Manual install and `--dry-run` / `-WhatIf` are documented in the README.

## Files in this release
- `fusion-lens-threads-v1.0.0.zip` — everything you need (installers + XML + READMEs + tests).
- `LensSizeThreads.xml` — the generated thread definition, for manual copy.

GitHub also attaches automatic `Source code (zip)` / `Source code (tar.gz)` archives.

## Docs
- README (English): https://github.com/HairuoLiu/fusion-lens-threads#readme
- README (中文): https://github.com/HairuoLiu/fusion-lens-threads/blob/main/README.zh-CN.md
- Reddit launch guide: `REDDIT.md`

## License
MIT — see `LICENSE`. SPDX: `MIT`.
