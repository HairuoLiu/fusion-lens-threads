SUBREDDIT: r/functionalprint
TYPE: self (text) post
LABEL: Primary — functional 3D prints

TITLE:
Printed a lens step-up ring / filter adapter? This adds real 42×1mm & 39×0.75mm threads to Fusion 360 so it actually screws on

SELF TEXT:
A lot of functional prints are camera accessories — step-up rings, lens caps, filter adapters, body caps. The problem is Fusion 360's thread tool doesn't include the camera sizes, so people model fake "threads" that don't mesh.

I open-sourced a thread library that fixes this:
- 73 sizes (24–127 mm), including 39 mm and 42 mm filter threads.
- 0.75 mm pitch (filters) and 1.0 mm pitch (M42 mount) for every size.
- Real external + internal threads with proper clearance, so a printed ring screws onto a real lens.

Install:
- macOS:  bash install_mac.sh
- Windows:  .\install_windows.ps1
- Restart Fusion 360 → Create › Thread → "镜头尺寸螺纹规格".

Download (ZIP): https://github.com/HairuoLiu/fusion-lens-threads/releases/download/v1.0.0/fusion-lens-threads-v1.0.0.zip
MIT licensed. Feedback / PRs welcome — especially if your size or pitch is missing.

FIRST COMMENT:
ZIP: https://github.com/HairuoLiu/fusion-lens-threads/releases/download/v1.0.0/fusion-lens-threads-v1.0.0.zip
Repo: https://github.com/HairuoLiu/fusion-lens-threads
