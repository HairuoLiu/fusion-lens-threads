SUBREDDIT: r/opensource
TYPE: self (text) post
LABEL: Secondary — open-source community

TITLE:
[OC] I open-sourced a Fusion 360 thread library for camera lens/filter sizes (MIT, zero deps, Mac + Windows)

SELF TEXT:
Sharing a small, focused open-source project: a Fusion 360 thread definition that adds 73 camera lens/filter thread sizes (24–127 mm) with 0.75 mm and 1.0 mm pitches, external + internal, to the built-in Thread tool.

Why: Fusion 360 ships without the common photo sizes (39/40/42/43 mm filters, M42×1 mount), so people model fake threads that don't mesh with real glass.

Highlights:
- Zero runtime dependencies — pure bash (macOS) and PowerShell (Windows) installers that auto-detect Fusion's ThreadData folder.
- Fully tested: a Python generator + test suite assert all three code paths (Python / bash / PowerShell) emit byte-identical, schema-valid XML.
- Bilingual README (EN + 中文), MIT licensed (SPDX: MIT).

Repo: https://github.com/HairuoLiu/fusion-lens-threads
Download (ZIP): https://github.com/HairuoLiu/fusion-lens-threads/releases/download/v1.0.0/fusion-lens-threads-v1.0.0.zip

Would love feedback on coverage (missing sizes/pitches) or the installer logic.

FIRST COMMENT:
ZIP: https://github.com/HairuoLiu/fusion-lens-threads/releases/download/v1.0.0/fusion-lens-threads-v1.0.0.zip
Repo: https://github.com/HairuoLiu/fusion-lens-threads
