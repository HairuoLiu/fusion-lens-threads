SUBREDDIT: r/functionalprint
TYPE: self (text) post + attach screenshots
LABEL: 第一梯队 #3 — 适配器专属
WHEN: Day 2

TITLE:
[OC] Free Fusion 360 thread library for lens/filter adapters — 73 sizes (M24–M127), 0.75 & 1.0 mm, so prints actually fit

SELF TEXT:
If you print lens adapters, step-up rings, or filter holders, you've hit the wall: Fusion 360's Thread tool doesn't include camera sizes. You end up faking the thread or hand-modeling it.

I made an open-source fix — a thread definition + one-script installers (Mac/Windows) that adds 73 camera thread diameters to Fusion's Thread feature:
- 0.75 mm (filter threads) and 1.0 mm (e.g. M42×1 mount), external + internal.
- Correct 0.10 mm clearance baked in, so an external part screws into an internal one without tweaking.
- One family in the dropdown: "Camera Lens and Filter Threads".

Useful for: step-up rings, lens hoods, body caps, filter→lens adapters, vintage-mount adapters.

Install: run the script for your OS → restart Fusion → Create › Thread → pick the family. MIT, zero dependencies.

(Links in first comment.)

FIRST COMMENT:
👉 ZIP (v1.0.0): https://github.com/HairuoLiu/fusion-lens-threads/releases/download/v1.0.0/fusion-lens-threads-v1.0.0.zip
👉 Repo: https://github.com/HairuoLiu/fusion-lens-threads
