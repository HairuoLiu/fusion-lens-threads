# fusion-lens-threads 全平台发布策略

> 本文件覆盖 **X (Twitter)**、**Reddit**、**Printables**、**Maker Forums**、**Facebook**、**Hackaday.io**、**Instructables**、**LinkedIn**、**CSDN/知乎**。
> 每个平台列出：发什么、怎么发、配哪些图、文案模板。

---

## 一、平台总览与核心资源

**下载直链（v1.0.0 ZIP）：**
https://github.com/HairuoLiu/fusion-lens-threads/releases/download/v1.0.0/fusion-lens-threads-v1.0.0.zip

**GitHub 仓库（双语 README + 7 张截图）：**
https://github.com/HairuoLiu/fusion-lens-threads

**可用配图（7 张）：**

| 文件名 | 内容 | 最佳用途 |
|--------|------|----------|
| `banner.svg` | 项目横幅 | X 头图、网站 banner |
| `thread-type-dropdown.png` | Fusion 螺纹下拉框出现本库 | **核心截图**，所有平台必用 |
| `thread-geometry.svg` | ISO 60° 牙型示意图 | 技术类平台（Hackaday、Instructables） |
| `designation-list.png` | 规格下拉两种螺距并列 | 说明"为什么两种螺距"时用 |
| `install-windows.png` | Windows 安装截图 | Windows 用户场景（Reddit、论坛） |
| `fusion-create-thread.png` | 创建螺纹对话框 | 教程类平台（Instructables、CSDN） |
| `result-part.png` | 建模螺纹最终效果 | **结果展示**，所有平台推荐用 |

> **图片选配策略（3 张一组最佳）**：
> `thread-type-dropdown.png` → `fusion-create-thread.png` → `result-part.png`

---

## 二、X (Twitter)

### 发帖形式
- **1 条置顶推文**（挂图 + 链接）
- **1 条回复串（thread）**（3–4 条展开说明）

### 推文 #1 — 置顶帖（短平快）

```
I got tired of hand-modeling lens & filter threads in Fusion 360.
So I built an open-source library that adds all 73 sizes (M24–M127) with 0.75 & 1.0mm pitch.

One script to install. MIT. Free.

🔗 https://github.com/HairuoLiu/fusion-lens-threads
```

**配图：** `thread-type-dropdown.png`

---

### 推文 #2 — Thread 开篇

```
🧵 Thread: I built a free Fusion 360 thread library for camera lenses & filters.

If you 3D-print lens adapters, step-up rings, or filter holders, you've dealt with this problem:

Fusion 360's Thread tool doesn't have a single camera size.

So I fixed it.👇
```

**配图：** `thread-type-dropdown.png`

---

### 推文 #3 — Thread 第 2 条

```
What's inside:
• 73 diameters — 24mm to 127mm (49, 52, 58, 67, 72, 77, 82, 95, 105, 127mm…)
• 0.75mm pitch for filter threads
• 1.0mm pitch for lens mounts (M42×1, M39×1)
• External + Internal for every size
• 0.10mm clearance → parts actually screw together

All in ONE dropdown. 30 seconds to install.
```

**配图：** `designation-list.png`

---

### 推文 #4 — Thread 第 3 条

```
macOS: bash install_mac.sh
Windows: .\install_windows.ps1
Restart Fusion → Create > Thread → "Camera Lens and Filter Threads"

No Python. No dependencies. MIT licensed. 
Star/fork if it saves you time: https://github.com/HairuoLiu/fusion-lens-threads

#Fusion360 #3Dprinting #CAD #OpenSource
```

**配图：** `fusion-create-thread.png` + `result-part.png`（两张拼图）

---

### X/Twitter 标签推荐
`#Fusion360` `#3Dprinting` `#CAD` `#OpenSource` `#Photography` `#3DPrint` `#Makers` `#DIY`

---

## 三、Reddit（已有完整草稿）

### 已有文件
已准备 11 个板块的独立帖子草稿 + 发帖节奏指南：
**`reddit-posts/POSTING-KIT.md`** | **`reddit-posts/README.md`**

### 板块列表（按节奏）

| 天 | 板块 | 备注 |
|----|------|------|
| Day 1 | r/Fusion360 → r/3Dprinting（间隔 3h） | 最精准 + 最大流量 |
| Day 2 | r/functionalprint → r/AnalogCommunity | 功能件 + 胶片圈 |
| Day 3 | r/vintagelenses → r/AdaptedLenses → r/mirrorless | 老镜头圈 |
| Day 4 | r/3DPrintingCommunity → r/opensource → r/CAD | 开发者 + 泛 CAD |
| Day 5 | r/photography → r/DIY（⚠️ 严格自推规则） | 超大量但风险高 |

### 核心规则
- 每条帖子**标题和正文不一样**（否则 Reddit 的 safe-mode 会去重拦截）
- 建帖时挂 `thread-type-dropdown.png` + `fusion-create-thread.png` + `install-windows.png` 三张图
- 链接放**第一条评论**，正文不放裸链
- 标 `[OC]`
- 每天 2–3 个，跨 5 天发完

---

## 四、Printables.com（Prusa 官方平台）

### 为什么发这里
- 你的竞品（sbuerger 的 "Photo thread library"）就在 Printables 上，有 12 条评价
- Printables 有奖励系统，上传模型可赚 filament
- 3D 打印社区的核心聚集地

### 发帖形式
发布为 **3D Model / Tool**（不是打印件，而是 CAD 工具资源）

### 标题
> Fusion 360 Camera Lens & Filter Thread Library — 73 Sizes, 0.75 & 1.0mm Pitch

### 描述（Description）
```
📷 What it is

A one-click custom thread library that adds every common camera-lens and filter thread (M39, M40, M42, M43 … up to 127 mm) to Autodesk Fusion 360 — each in both 0.75 mm and 1.0 mm pitch, with proper clearance so parts actually screw together.

🔧 Why you need it

Fusion 360 ships with standard ISO / UTS thread tables, but photographic lens and filter threads are not in there. If you 3D-print or machine lens adapters, filter rings, step-up rings, or custom mounts, you normally have to hand-model each thread. This drops a ready-made thread family into Fusion so you can just pick the size and pitch from the dropdown.

📦 What's included
- 73 diameters covering 24 – 127 mm
- Two pitches per size — 0.75 mm (filter threads) and 1.0 mm (M42×1 mount etc.)
- External (6g) + internal (6H) for every entry, with 0.10 mm fit clearance
- macOS installer (bash) and Windows installer (PowerShell) — both auto-detect your Fusion ThreadData folder
- Pre-built XML ready to use

⚙️ How to install

macOS:
1. Run: bash install_mac.sh
2. Restart Fusion 360
3. Create > Thread > pick "Camera Lens and Filter Threads"

Windows:
1. Run: powershell -ExecutionPolicy Bypass -File install_windows.ps1
2. Restart Fusion 360
3. Create > Thread > pick "Camera Lens and Filter Threads"

📜 License: MIT (free to use, modify, share)

🔗 GitHub: https://github.com/HairuoLiu/fusion-lens-threads
```

### 配图（Printables 支持多图）
按顺序上传：
1. `thread-type-dropdown.png`（首图）
2. `fusion-create-thread.png`
3. `result-part.png`
4. `designation-list.png`
5. `install-windows.png`

### 标签
`Fusion360`, `thread`, `camera`, `lens`, `filter`, `adapter`, `M42`, `photography`, `CAD`, `opensource`

---

## 五、Maker Forums (forum.makerforums.info)

### 形式
发在 **「3D Printing」** 分类下

### 标题
> Free Fusion 360 thread library for camera lens & filter sizes — 73 diameters, 0.75 & 1.0 mm pitch

### 正文
```
I built an open-source tool for Fusion 360 that adds 73 common camera lens/filter thread sizes (M24–M127) with both 0.75 mm and 1.0 mm pitch, external + internal, with proper clearance.

It ships as a ready-to-use XML file + one-line installers for macOS and Windows. No Python, no dependencies, just run the script and restart Fusion.

What it's good for:
- Step-up rings, lens caps, filter adapters
- M42×1 / M39×1 lens mount adapters
- Custom lens hoods and body caps
- Any threaded camera accessory

Install (≈30 seconds):
1. Download from GitHub (link below)
2. Run the installer for your OS
3. Restart Fusion 360 → Create > Thread → pick "Camera Lens and Filter Threads"

MIT licensed. PRs welcome for additional sizes or Linux support.

🔗 https://github.com/HairuoLiu/fusion-lens-threads
```
**配图：** 上 `thread-type-dropdown.png` + `result-part.png`

---

## 六、Facebook Groups

### 推荐群组
| 群组 | 发帖方式 | 说明 |
|------|----------|------|
| **3D Printing Functional Things** | 文字 + 图 | 功能件社群，发成果图 + 工具链接 |
| **Fusion 360 Users** | 文字 + 图 | CAD 用户精准受众 |
| **3D Printing for Beginners and Pros** | 文字 + 图 | 大群，发精华版 |

### 统一文案（可套用）
```
🛠️ Just released a free open-source tool for Fusion 360!

It adds ALL common camera lens & filter threads (M24–M127, 73 sizes) with 0.75mm and 1.0mm pitch — external + internal with correct clearance so printed parts actually screw together.

One-click install for Mac & Windows. MIT licensed. No signup needed.

If you 3D-print lens adapters, step-up rings, or filter holders, this will save you hours.

👇 Download + repo in the comments.
```
**配图：** 选 1–3 张（`thread-type-dropdown.png` + `result-part.png`）

**评论里放：**
```
👉 ZIP download: https://github.com/HairuoLiu/fusion-lens-threads/releases/download/v1.0.0/fusion-lens-threads-v1.0.0.zip
👉 GitHub repo (with full README + screenshots): https://github.com/HairuoLiu/fusion-lens-threads
```

---

## 七、Hackaday.io

### 形式
创建一个 **Project** 页面（不是 Blog 帖）

### 项目名称
> fusion-lens-threads — Custom Camera Thread Library for Fusion 360

### 项目简介（Summary）
> A one-click open-source thread library that adds 73 common camera lens & filter thread sizes (M24–M127) to Autodesk Fusion 360. macOS & Windows installers, zero dependencies, MIT licensed.

### 项目详情（Details）
```
Fusion 360 ships with standard ISO/UTS threads but not a single photographic lens or filter thread. If you design lens adapters, step-up rings, filter holders, or custom camera accessories, you've had to hand-model each thread — until now.

This project provides a custom thread family ("Camera Lens and Filter Threads") that drops into Fusion 360's built-in Thread tool. 73 diameters from 24 mm to 127 mm, each available in 0.75 mm (filter) and 1.0 mm (lens mount) pitch, with proper 6g/6H clearance.

Key features:
- Auto-detecting installers for macOS (bash) and Windows (PowerShell)
- 73 sizes × 2 pitches × (external + internal) = 292 thread definitions
- 0.10 mm fit clearance so parts actually screw together
- Pure XML — no plugins, no Python needed to install
- Three generators (Python/bash/PowerShell) verified byte-for-byte identical
- MIT license — free to use, modify, and share

The project includes a Python generator for customizing sizes/pitches, a pre-built XML for manual install, and a test suite to validate geometry across all generators.
```

### 配图
1. `thread-type-dropdown.png`（封面）
2. `thread-geometry.svg`
3. `result-part.png`

---

## 八、Instructables

### 形式
**教程型帖子**（步骤清晰、图文并茂）

### 标题
> Add Every Camera Lens Thread to Fusion 360 — Free Open-Source Library

### 步骤大纲

**Step 1: The Problem**
> Fusion 360's Thread tool is missing camera lens & filter threads. Here's the fix.
配图: `thread-type-dropdown.png`（缩放至 600px）

**Step 2: Download the Files**
> Clone or download the ZIP from GitHub.
> 🔗 https://github.com/HairuoLiu/fusion-lens-threads
配图: 无（纯说明）

**Step 3: Install on macOS**
> ```bash
> chmod +x install_mac.sh
> ./install_mac.sh
> ```

**Step 4: Install on Windows**
> ```powershell
> powershell -ExecutionPolicy Bypass -File install_windows.ps1
> ```
配图: `install-windows.png`

**Step 5: Use It in Fusion 360**
> Restart Fusion → Create > Thread → set Thread Type to "Camera Lens and Filter Threads" → pick your size.
配图: `fusion-create-thread.png`

**Step 6: The Result**
> Fully modeled thread, ready to 3D print or machine.
配图: `result-part.png`

**Step 7: Which Pitch?**
> 0.75 mm = filter threads (UV/ND/CPL filters, lens caps) | 1.0 mm = lens mounts (M42×1, M39×1) + large filter diameters (≥95mm)
配图: `designation-list.png`

---

## 九、LinkedIn

### 形式
① 一篇图文帖 → ② 评论区补链接

### 帖子文案

```
📷 I open-sourced a Fusion 360 thread library for camera lenses and filters.

If you design or 3D-print lens adapters, step-up rings, or camera accessories, you've probably noticed that Fusion 360's built-in threads don't include any photographic sizes — M42 mount, M39, 49mm filter, 77mm filter, etc.

So I built a custom thread family that adds all 73 common sizes (24–127mm) with both 0.75mm (filter) and 1.0mm (mount) pitch.

The installers auto-detect your Fusion folder — one command, restart, done. Mac & Windows supported.

Key stats:
🔩 73 diameters × 2 pitches × 2 genders = 292 thread definitions
📐 ISO 60° profile with 0.10mm fit clearance
🪶 Zero runtime dependencies (pure bash/PowerShell)
🧪 Cross-verified generators (Python/bash/PowerShell output identical)
📜 MIT licensed

Free for anyone to use. PRs and issues welcome.

🔗 https://github.com/HairuoLiu/fusion-lens-threads

#Fusion360 #3DPrinting #OpenSource #CAD #Photography #MechanicalDesign #Engineering
```

**配图：** `banner.svg`（封面）+ `thread-type-dropdown.png`

---

## 十、CSDN / 知乎（中文平台）

### CSDN 帖子
#### 标题
> Fusion 360 缺少镜头螺纹？我做了个免费开源库，73种尺寸一键安装

#### 正文
```
如果你用 Fusion 360 设计镜头转接环、滤镜升降环或镜头盖，你肯定遇到过这个问题：

Fusion 360 自带的螺纹库里一个摄影螺纹都没有。M42×1 卡口？没有。49mm 滤镜螺纹？也没有。每次只能手画。

所以我做了个开源工具：

📦 73 种直径（24–127mm），涵盖所有常见镜头/滤镜尺寸
🎯 每种直径同时支持 0.75mm（滤镜螺纹）和 1.0mm（卡口螺纹）
🔩 内螺 + 外螺，0.10mm 配合间隙，打印出来能真的拧上
⚡ 一键安装脚本（Mac + Windows），自动找到 Fusion 的 ThreadData 目录

安装只需要三步：
1. 下载 ZIP 或 git clone
2. 运行安装脚本（Mac: bash install_mac.sh / Windows: .\install_windows.ps1）
3. 重启 Fusion → 创建 → 螺纹 → 选 "Camera Lens and Filter Threads"

MIT 协议，随便用随便改。

GitHub: https://github.com/HairuoLiu/fusion-lens-threads
```

**配图：** `thread-type-dropdown.png` + `fusion-create-thread.png`

---

### 知乎
#### 标题
> Fusion 360 缺少镜头螺纹？我做了个开源库，73 种尺寸一键添加

#### 回答/文章
同 CSDN 文案，额外加一段个人背景：
```
我是刘海若，腾讯产品经理，滑铁卢 ECE MEng 在读。这个工具是我 3D 打印镜头转接环时顺手做的，觉得应该也有人需要，就开源了。

如果你也在做相机配件设计，欢迎用用看，提 PR 或 issue。
```

---

## 十一、总结：发帖节奏

| 周次 | 平台 | 内容 | 频次 |
|------|------|------|------|
| **第 1 天** | X (Twitter) + LinkedIn | 同步发 | 各 1 条 |
| **第 1 天** | r/Fusion360 | Reddit 首发 | 1 帖 |
| **第 2 天** | r/3Dprinting + r/functionalprint | Reddit 续发 | 2 帖 |
| **第 2 天** | Printables.com | 创建项目页 | 1 次 |
| **第 3 天** | r/AnalogCommunity + r/vintagelenses | Reddit 续发 | 2 帖 |
| **第 3 天** | Hackaday.io | 创建项目页 | 1 次 |
| **第 4 天** | r/AdaptedLenses + r/mirrorless + r/opensource | Reddit 续发 | 3 帖 |
| **第 4 天** | Maker Forums | 发帖 | 1 次 |
| **第 5 天** | Facebook Groups (Fusion 360 Users 等) | 发帖 | 2–3 群 |
| **第 5 天** | Instructables | 发布教程 | 1 次 |
| **第 5 天+** | r/photography + r/DIY | Reddit 慎发 | 1–2 帖 |
| **第 6 天** | CSDN + 知乎 | 中文平台 | 各 1 篇 |

### 核心原则
1. **图片优先** — 每个帖子至少挂 1 张图，Reddit / X 建议 3 张
2. **链接放评论** — 正文不放裸链的平台（Reddit 多数板块、Facebook）把链接放首评
3. **不同平台不同文案** — 不要复制粘贴，改标题、改第一段，否则被判定为 spam
4. **回复评论** — 发帖后 2 小时内回复每条评论，增加曝光
5. **双向引流** — GitHub → Reddit/论坛，Reddit/论坛 → GitHub Star
