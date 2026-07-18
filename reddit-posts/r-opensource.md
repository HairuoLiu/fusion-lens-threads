SUBREDDIT: r/opensource
TYPE: self (text) post + attach screenshots
LABEL: 第二梯队 — 开发者/FOSS 曝光
WHEN: Day 4

TITLE:
[OC] I open-sourced a Fusion 360 thread library for camera lens/filter sizes (73 sizes, MIT, zero deps)

SELF TEXT:
Small but genuinely useful: Fusion 360 ships standard ISO/UTS threads but not photographic lens/filter threads (M42 mount, M39, the dozens of filter diameters). I built a thread-definition XML + one-line Mac/Windows installers that drop 73 sizes (24–127 mm) into the built-in Thread feature, each in 0.75 mm and 1.0 mm pitch with proper 6g/6H clearance.

- Pure XML + bash/PowerShell, no Python needed to install.
- Three generators (Python/bash/PowerShell) verified byte-identical by a test harness.
- MIT licensed.

Useful if you 3D-print or machine lens adapters, step-up rings, caps.

Download + source (first comment).

FIRST COMMENT:
👉 ZIP (v1.0.0): https://github.com/HairuoLiu/fusion-lens-threads/releases/download/v1.0.0/fusion-lens-threads-v1.0.0.zip
👉 Source + bilingual README: https://github.com/HairuoLiu/fusion-lens-threads
PRs welcome (extra sizes/pitches, Linux path detection).
