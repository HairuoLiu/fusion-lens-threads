SUBREDDIT: r/Fusion360
TYPE: self (text) post
LABEL: Primary — CAD audience

TITLE:
[Free] Add lens & filter thread sizes (M24–M127, 0.75 & 1.0 mm pitch) to Fusion 360's Thread tool — one script, zero dependencies

SELF TEXT:
If you've ever tried to model a lens cap, step-up ring, or filter adapter in Fusion 360, you know the built-in thread library is missing the common camera sizes. So I built a small open-source add-on.

What it adds:
- 73 lens/filter diameters from 24 mm to 127 mm (39, 40, 42, 43, 46, 49, 52, 55, 58, 62, 67, 72, 77, 82, 86, 95, 105, 112, 127…).
- Two pitches per size: 0.75 mm (filter threads) and 1.0 mm (e.g. M42×1 mount), so parts actually screw together.
- External (bolt) + internal (hole) threads for every size, with correct 6g/6H clearance.
- A single new thread family in Fusion: "Camera Lens and Filter Threads" (Lens Size Threads).

Install (≈30s):
1. macOS:  bash install_mac.sh
2. Windows (PowerShell):  .\install_windows.ps1
3. Restart Fusion 360 → Create › Thread → pick "Camera Lens and Filter Threads".

Both installers auto-detect Fusion's ThreadData folder (newest version) and drop the XML there. Manual install + dry-run are documented in the README.

Download: https://github.com/HairuoLiu/fusion-lens-threads/releases/download/v1.0.0/fusion-lens-threads-v1.0.0.zip
Repo + docs: https://github.com/HairuoLiu/fusion-lens-threads
License: MIT

FIRST COMMENT (if the sub restricts links in the body):
👉 Download (ZIP, v1.0.0): https://github.com/HairuoLiu/fusion-lens-threads/releases/download/v1.0.0/fusion-lens-threads-v1.0.0.zip
Source + bilingual README: https://github.com/HairuoLiu/fusion-lens-threads
