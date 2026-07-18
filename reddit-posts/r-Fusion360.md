SUBREDDIT: r/Fusion360
TYPE: self (text) post + attach the 3 screenshots
LABEL: 第一梯队 #1 — 最精准受众
WHEN: Day 1, 美东时间 9:00–12:00（周二/三最佳）

TITLE:
Stop hand-modeling lens & filter threads in Fusion 360 — free library adds 73 sizes (M24–M127), both 0.75 & 1.0 mm pitch

SELF TEXT:
If you've ever tried to model a lens cap, step-up ring, or filter adapter in Fusion 360, you know the built-in thread library is missing every common camera size. So I built a small open-source add-on — one script, zero dependencies, done in ~30 seconds.

What it adds to the Thread tool:
- 73 lens/filter diameters, 24–127 mm (39, 40, 42, 43, 46, 49, 52, 55, 58, 62, 67, 72, 77, 82, 86, 95, 105, 112, 127…).
- Two pitches per size: 0.75 mm (filter threads) and 1.0 mm (e.g. M42×1 mount), so parts actually screw together.
- External (6g) + internal (6H) for every size, with correct 0.10 mm clearance baked in.
- A single new family in the Thread Type dropdown: "Camera Lens and Filter Threads".

Install:
1. macOS:  bash install_mac.sh
2. Windows (PowerShell):  .\install_windows.ps1
3. Restart Fusion 360 → Create › Thread → pick "Camera Lens and Filter Threads".

Both installers auto-detect Fusion's ThreadData folder (newest version) and drop the XML there. Screenshots show it live in the dialog. MIT licensed, no signup.

(Download + bilingual README in the first comment.)

FIRST COMMENT (put the links here — some subs filter body URLs):
👉 Download (ZIP, v1.0.0, one click): https://github.com/HairuoLiu/fusion-lens-threads/releases/download/v1.0.0/fusion-lens-threads-v1.0.0.zip
👉 Repo + docs (with the screenshots): https://github.com/HairuoLiu/fusion-lens-threads
License: MIT. Star it if it saves you time.
