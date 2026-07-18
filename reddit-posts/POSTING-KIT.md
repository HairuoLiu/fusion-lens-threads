# Reddit 发帖包（复制粘贴即可发）

> 用途：Reddit 已关闭自助 API 建 app，且网关拦截自动化浏览器，所以**自动化发帖走不通**。
> 这份包是给你**手动发帖**用的——每条都是现成的标题 + 正文 + 第一条评论，复制粘贴即可。
>
> 下载直链（v1.0.0，含修复后的安装器 + 三张截图）：
> https://github.com/HairuoLiu/fusion-lens-threads/releases/download/v1.0.0/fusion-lens-threads-v1.0.0.zip
> 仓库：https://github.com/HairuoLiu/fusion-lens-threads

## 发帖节奏（避免被当 spam）
- **每天发 2–3 个，跨 4–5 天**，别同一小时全撒。
- 主帖有了几条评论后，用 Reddit 自带 **Crosspost** 转到其他对口板块，比新开帖更稳。
- 建帖时**挂上这 3 张截图**（视觉证明，转化率高）：
  - `thread-type-dropdown.png`（螺纹类型下拉出现本库）
  - `fusion-create-thread.png`（创建螺纹对话框）
  - `install-windows.png`（右键 → 用 PowerShell 运行）
- 多数板块把**链接放「第一条评论」**最安全（正文裸链常被自动移除）。
- 发帖后 **2 小时内秒回评论**，把帖子顶上 rising。
- 标 `[OC]`，原创内容更被宽容。
- 最佳时段：周二~周四 美东 9:00–12:00 或 18:00–21:00。

---

### 1. r/Fusion360 — 第一梯队 #1（Day 1，美东 9–12）
**标题：**
```
Stop hand-modeling lens & filter threads in Fusion 360 — free library adds 73 sizes (M24–M127), both 0.75 & 1.0 mm pitch
```
**正文：**
```
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
```
**第一条评论：**
```
👉 Download (ZIP, v1.0.0, one click): https://github.com/HairuoLiu/fusion-lens-threads/releases/download/v1.0.0/fusion-lens-threads-v1.0.0.zip
👉 Repo + docs (with the screenshots): https://github.com/HairuoLiu/fusion-lens-threads
License: MIT. Star it if it saves you time.
```

---

### 2. r/3Dprinting — 第一梯队 #2（Day 1，与 #1 隔 3–4 小时）
**标题：**
```
[OC] I kept seeing "threads" on printed lens adapters that weren't real threads — so I made a free Fusion 360 thread library (73 sizes, M24–M127)
```
**正文：**
```
Sharing a small tool because the 3D-printed lens-accessory world is full of fake threads.

It's a Fusion 360 thread definition (XML) + one-line installers for Mac & Windows that drops 73 camera thread sizes straight into the built-in Thread feature:
- Filter + mount sizes: 39, 40, 42, 43, 46, 49, 52, 55, 58, 62, 67, 72, 77, 82, 86, 95, 105, 112, 127…
- Pitches: 0.75 mm and 1.0 mm, external + internal, with proper 6g/6H clearance so your printed parts ACTUALLY screw together.
- No dependencies, MIT licensed, no signup.

Great for step-up rings, lens hoods, body caps, filter → lens adapters. Screenshots show it live in the dialog.

How to use (≈30s):
1. Download & run the installer for your OS.
2. Restart Fusion 360.
3. Create › Thread → choose "Camera Lens and Filter Threads".

(Links in the first comment.)
```
**第一条评论：**
```
👉 Download (ZIP, v1.0.0, one click): https://github.com/HairuoLiu/fusion-lens-threads/releases/download/v1.0.0/fusion-lens-threads-v1.0.0.zip
👉 Repo + README with the screenshots: https://github.com/HairuoLiu/fusion-lens-threads
```

---

### 3. r/functionalprint — 第一梯队 #3（Day 2）
**标题：**
```
[OC] Free Fusion 360 thread library for lens/filter adapters — 73 sizes (M24–M127), 0.75 & 1.0 mm, so prints actually fit
```
**正文：**
```
If you print lens adapters, step-up rings, or filter holders, you've hit the wall: Fusion 360's Thread tool doesn't include camera sizes. You end up faking the thread or hand-modeling it.

I made an open-source fix — a thread definition + one-script installers (Mac/Windows) that adds 73 camera thread diameters to Fusion's Thread feature:
- 0.75 mm (filter threads) and 1.0 mm (e.g. M42×1 mount), external + internal.
- Correct 0.10 mm clearance baked in, so an external part screws into an internal one without tweaking.
- One family in the dropdown: "Camera Lens and Filter Threads".

Useful for: step-up rings, lens hoods, body caps, filter→lens adapters, vintage-mount adapters.

Install: run the script for your OS → restart Fusion → Create › Thread → pick the family. MIT, zero dependencies.

(Links in first comment.)
```
**第一条评论：**
```
👉 ZIP (v1.0.0): https://github.com/HairuoLiu/fusion-lens-threads/releases/download/v1.0.0/fusion-lens-threads-v1.0.0.zip
👉 Repo: https://github.com/HairuoLiu/fusion-lens-threads
```

---

### 4. r/AnalogCommunity — 第一梯队 #4（Day 2）
**标题：**
```
[OC] Free Fusion 360 thread library for lens caps & adapters — M39, M42, 39/42mm filters, 73 sizes total, 0.75 & 1.0 mm
```
**正文：**
```
For those of us who 3D-print lens caps, hoods, and focal-shift rigs for vintage glass: Fusion 360 doesn't ship the thread sizes we need (M42×1, M39×1, 39/42mm filter threads). I put together an open-source thread library.

Coverage:
- 73 diameters 24–127 mm, including the all-important M42 mount and 39/42 mm filters.
- 0.75 mm and 1.0 mm pitch, external + internal, with correct clearance.
- One Fusion thread family: "Camera Lens and Filter Threads".

Install:
- macOS:  bash install_mac.sh
- Windows:  .\install_windows.ps1
- Restart Fusion → Create › Thread → pick it.

MIT licensed. If you model a specific adapter, I'd love to see it. (Links in first comment.)
```
**第一条评论：**
```
👉 ZIP (v1.0.0): https://github.com/HairuoLiu/fusion-lens-threads/releases/download/v1.0.0/fusion-lens-threads-v1.0.0.zip
👉 Repo: https://github.com/HairuoLiu/fusion-lens-threads
```

---

### 5. r/vintagelenses — 第一梯队 #5（Day 3）
**标题：**
```
Made a free Fusion 360 thread library for M42, M39, 42mm & 39mm filter threads — so your adapted/vintage glass models screw together properly
```
**正文：**
```
For those of us who 3D-print lens adapters, caps, and focus rigs for vintage glass: Fusion 360 doesn't ship the thread sizes we need (M42×1, M39×1, 39mm/42mm filter threads). I put together an open-source thread library.

Coverage:
- 73 diameters 24–127 mm, including the all-important M42 mount and 39/42 mm filters.
- 0.75 mm and 1.0 mm pitch, external + internal, with correct clearance.
- One Fusion thread family: "Camera Lens and Filter Threads".

Install:
- macOS:  bash install_mac.sh
- Windows:  .\install_windows.ps1
- Restart Fusion → Create › Thread → pick it.

MIT. If you model a specific adapter, I'd love to see it. (Links in first comment.)
```
**第一条评论：**
```
👉 ZIP (v1.0.0): https://github.com/HairuoLiu/fusion-lens-threads/releases/download/v1.0.0/fusion-lens-threads-v1.0.0.zip
👉 Repo: https://github.com/HairuoLiu/fusion-lens-threads
```

---

### 6. r/AdaptedLenses — 第二梯队（Day 3）
**标题：**
```
[OC] Free Fusion 360 thread library for lens adapters — M42×1, M39×1, 39/42mm filters, 73 sizes, 0.75 & 1.0 mm
```
**正文：**
```
For everyone here printing adapted-lens adapters, caps, and rigs: Fusion 360 doesn't include the camera thread sizes we use (M42×1, M39×1, 39/42mm filter threads). I made an open-source thread library to fix that.

What you get:
- 73 diameters 24–127 mm, including the key M42 mount and 39/42 mm filters.
- 0.75 mm and 1.0 mm pitch, external + internal, with correct clearance.
- One Fusion thread family: "Camera Lens and Filter Threads".

Install:
- macOS:  bash install_mac.sh
- Windows:  .\install_windows.ps1
- Restart Fusion → Create › Thread → pick it.

MIT. Show me what you adapt. (Links in first comment.)
```
**第一条评论：**
```
👉 ZIP (v1.0.0): https://github.com/HairuoLiu/fusion-lens-threads/releases/download/v1.0.0/fusion-lens-threads-v1.0.0.zip
👉 Repo: https://github.com/HairuoLiu/fusion-lens-threads
```

---

### 7. r/mirrorless — 第二梯队（Day 3）
**标题：**
```
[OC] Free Fusion 360 thread library for adapted-lens accessories — 73 sizes (M24–M127), 0.75 & 1.0 mm pitch
```
**正文：**
```
If you print adapters, step-up rings, or caps for your adapted glass, you've hit it: Fusion 360's Thread tool doesn't include camera sizes. I made an open-source fix.

What it adds:
- 73 diameters 24–127 mm, 0.75 mm (filter) + 1.0 mm (M42×1 mount etc.), external + internal.
- Correct 0.10 mm clearance so printed parts actually screw together.
- One family in the dropdown: "Camera Lens and Filter Threads".

Install: run the Mac/Windows script → restart Fusion → Create › Thread → pick it. MIT, zero dependencies.

(Links in first comment.)
```
**第一条评论：**
```
👉 ZIP (v1.0.0): https://github.com/HairuoLiu/fusion-lens-threads/releases/download/v1.0.0/fusion-lens-threads-v1.0.0.zip
👉 Repo: https://github.com/HairuoLiu/fusion-lens-threads
```

---

### 8. r/3DPrintingCommunity — 第二梯队（Day 4）
**标题：**
```
[OC] Free Fusion 360 thread library so your printed lens adapters actually screw together (73 sizes, M24–M127)
```
**正文：**
```
Sharing a tool I wish existed sooner: a Fusion 360 thread definition + Mac/Windows installers that add 73 camera thread sizes (24–127 mm) to the built-in Thread feature — 0.75 mm and 1.0 mm pitch, external + internal, with proper clearance so prints fit.

Great for step-up rings, hoods, caps, filter adapters. One script, no dependencies, MIT.

How to use: run installer → restart Fusion → Create › Thread → "Camera Lens and Filter Threads". (Links in first comment.)
```
**第一条评论：**
```
👉 ZIP (v1.0.0): https://github.com/HairuoLiu/fusion-lens-threads/releases/download/v1.0.0/fusion-lens-threads-v1.0.0.zip
👉 Repo: https://github.com/HairuoLiu/fusion-lens-threads
```

---

### 9. r/opensource — 第二梯队（Day 4）
**标题：**
```
[OC] I open-sourced a Fusion 360 thread library for camera lens/filter sizes (73 sizes, MIT, zero deps)
```
**正文：**
```
Small but genuinely useful: Fusion 360 ships standard ISO/UTS threads but not photographic lens/filter threads (M42 mount, M39, the dozens of filter diameters). I built a thread-definition XML + one-line Mac/Windows installers that drop 73 sizes (24–127 mm) into the built-in Thread feature, each in 0.75 mm and 1.0 mm pitch with proper 6g/6H clearance.

- Pure XML + bash/PowerShell, no Python needed to install.
- Three generators (Python/bash/PowerShell) verified byte-identical by a test harness.
- MIT licensed.

Useful if you 3D-print or machine lens adapters, step-up rings, caps.

Download + source (first comment).
```
**第一条评论：**
```
👉 ZIP (v1.0.0): https://github.com/HairuoLiu/fusion-lens-threads/releases/download/v1.0.0/fusion-lens-threads-v1.0.0.zip
👉 Source + bilingual README: https://github.com/HairuoLiu/fusion-lens-threads
PRs welcome (extra sizes/pitches, Linux path detection).
```

---

### 10. r/photography — 第三梯队（Day 5+，⚠️ 自推规则极严，标 [OC]，链接只放首评）
**标题：**
```
[OC] I made a free Fusion 360 thread library for 3D-printed lens caps & adapters (73 sizes, MIT)
```
**正文：**
```
For photographers who 3D-print their own lens caps, hoods, and step-up rings: Fusion 360's Thread tool is missing every camera size, so most "threads" people print aren't real threads. I open-sourced a fix — 73 lens/filter diameters (24–127 mm), 0.75 & 1.0 mm pitch, with correct clearance so parts actually screw together. One script to install, MIT licensed, no signup.

Happy to answer questions about which pitch to use (spoiler: ≤86mm filters = 0.75mm, big filters + M42/M39 mounts = 1.0mm).

(The download + source are in the first comment, since this sub filters links in the body.)
```
**第一条评论：**
```
👉 Download (ZIP, v1.0.0): https://github.com/HairuoLiu/fusion-lens-threads/releases/download/v1.0.0/fusion-lens-threads-v1.0.0.zip
👉 Source + README: https://github.com/HairuoLiu/fusion-lens-threads
```

---

### 11. r/DIY — 第三梯队（Day 5+，⚠️ 自推规则严，标 [OC]，链接只放首评）
**标题：**
```
[OC] Free Fusion 360 thread library for DIY lens adapters & caps — 73 sizes, real threads that fit
```
**正文：**
```
If you DIY camera accessories (lens caps, step-up rings, filter adapters) and model them in Fusion 360, you've probably noticed the Thread tool lacks camera sizes. I made an open-source library that adds 73 of them (24–127 mm, 0.75 & 1.0 mm pitch) with real clearance, so your printed parts actually screw together. One installer script, MIT, no account needed.

(Download + source in the first comment — this sub filters body links.)
```
**第一条评论：**
```
👉 ZIP (v1.0.0): https://github.com/HairuoLiu/fusion-lens-threads/releases/download/v1.0.0/fusion-lens-threads-v1.0.0.zip
👉 Repo: https://github.com/HairuoLiu/fusion-lens-threads
```

---

## 可选：r/CAD / r/cad
没有单独草稿，可复用 **#9 r/opensource** 的文案（强调「自定义螺纹族 / XML + 脚本」的 CAD 工作流），把标题改成类似：
`[OC] Open-source Fusion 360 custom thread family for camera lens/filter sizes (73 sizes, MIT)`
