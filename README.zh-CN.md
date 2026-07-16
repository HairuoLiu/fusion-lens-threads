<!-- 语言切换 -->
[English](README.md) · **简体中文**

<p align="center">
  <img src="docs/images/banner.svg" alt="fusion-lens-threads — Autodesk Fusion 360 镜头 / 滤镜自定义螺纹库" width="100%">
</p>

<p align="center">
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg"></a>
  <img alt="Platform" src="https://img.shields.io/badge/platform-macOS%20%7C%20Windows-blue">
  <img alt="Dependencies" src="https://img.shields.io/badge/runtime%20deps-none-brightgreen">
  <img alt="Fusion 360" src="https://img.shields.io/badge/Autodesk-Fusion%20360-orange">
  <img alt="Threads" src="https://img.shields.io/badge/threads-73%20sizes%20%C3%97%202%20pitches-9cf">
</p>

> 一键为 Autodesk Fusion 360 添加**所有常见镜头 / 滤镜螺纹**（M39、M40、M42、M43…
> 直到 127 mm），每个尺寸同时提供 **0.75 mm 与 1.0 mm 两种螺距**，并预留配合间隙，
> 保证零件能真正拧到一起。附 macOS / Windows 安装脚本，零运行时依赖。

<p align="center">
  <!-- 📷 图片 #3（最关键的一张）：Fusion 螺纹对话框，「螺纹类型」下拉框展开，
       高亮显示「镜头尺寸螺纹规格」。详见 docs/images/README.md -->
  <img src="docs/images/thread-type-dropdown.png" alt="安装后「镜头尺寸螺纹规格」出现在 Fusion 360 螺纹类型下拉框中" width="720">
  <br><em>安装后，<strong>镜头尺寸螺纹规格</strong> 会直接出现在螺纹命令的「螺纹类型」里。</em>
</p>

---

## 目录

- [为什么做这个](#为什么做这个)
- [特性](#特性)
- [支持的尺寸与螺距](#支持的尺寸与螺距)
- [环境要求](#环境要求)
- [安装](#安装)
  - [macOS](#macos)
  - [Windows](#windows)
  - [手动安装（任意系统）](#手动安装任意系统)
- [在 Fusion 360 中使用](#在-fusion-360-中使用)
- [Fusion 更新之后](#fusion-更新之后)
- [常见问题](#常见问题)
- [原理](#原理)
- [二次开发 / 测试](#二次开发--测试)
- [参与贡献](#参与贡献)
- [开源协议](#开源协议)
- [致谢](#致谢)

---

## 为什么做这个

Fusion 360 自带标准的 ISO / UTS 螺纹表，但**没有摄影镜头 / 滤镜螺纹**——比如 M42
镜头卡口、M39（徕卡螺口），以及几十种滤镜口径（49、52、77 mm…）。如果你要 3D 打印
或加工镜头转接环、滤镜环、升降环、自定义卡口，通常只能手动逐个建模螺纹。

本项目把做好的螺纹族直接塞进 Fusion，你只需在下拉框里选尺寸和螺距即可，和内置螺纹
一样方便。

## 特性

- 🔍 **自动搜索** Fusion 360 的 `ThreadData` 目录（自动选最新已安装版本），
  macOS / Windows 均支持，无需在隐藏目录里翻找。
- 📦 **73 个直径**，覆盖常见镜头 / 滤镜全范围（24 – 127 mm）。
- 🎯 **每个尺寸两种螺距**——`0.75 mm` 与 `1.0 mm`（如 `M42x1` 卡口、`M42x0.75` 滤镜）。
- 🔩 每条都含**外螺纹 (6g) + 内螺纹 (6H)**，按 0.10 mm 配合间隙计算，
  同尺寸外螺可拧入内螺。
- 🪶 **零运行时依赖**——macOS 用系统自带 `bash`，Windows 用系统自带 `PowerShell`，
  安装时不需要 Python。
- 🧪 **已测试**——Python 生成器 + 测试脚本验证三个生成器（Python / bash / PowerShell）
  输出完全一致且为合法 Fusion XML。
- 🛠️ **易改**——改一行列表即可增删尺寸或螺距。

## 支持的尺寸与螺距

全部直径（mm），每个都提供 **0.75 mm** 与 **1.0 mm** 两种螺距：

```
24    25    25.5  27    28    30    30.5  34    35.5  36    36.5  37    37.5
38.5  39    40    40.5  41    42    43    43.5  44    46    46.5  48    49
50    50.5  52    54    55    56    58    60    62    64    67    70    72
74    75    76    77    78    80    82    84    85    86    87    90    92
94    95    96    98    100   102   104   105   107   108   110   112   114
116   118   120   122   124   125   126   127
```

即 **73 个尺寸 × 2 种螺距 ×（外螺 + 内螺）= 292 条螺纹定义**。你点名的 `M39`、
`M40`、`M42`、`M43` 全部包含。

<p align="center">
  <img src="docs/images/thread-geometry.svg" alt="ISO 米制 60° 螺纹牙型：螺距、大径 / 小径、配合间隙" width="720">
</p>

## 环境要求

- 已安装 Autodesk Fusion 360（较新版本均可）。
- macOS **或** Windows。默认安装不需要 Python、不需要插件、不需要管理员权限。

---

## 安装

> **一句话：** 跑一次脚本 → **重启 Fusion 360** → 在螺纹对话框里选
> `镜头尺寸螺纹规格`。三步搞定。

先获取文件——可以 **git clone**，也可以点 GitHub 绿色 `Code` 按钮 **下载 ZIP** 解压：

```bash
git clone https://github.com/HairuoLiu/fusion-lens-threads.git
cd fusion-lens-threads
```

### macOS

**第一步 — 运行安装脚本**

```bash
chmod +x install_mac.sh
./install_mac.sh
```

脚本会自动找到 Fusion 的 `ThreadData` 目录并写入 `LensSizeThreads.xml`。

<p align="center">
  <!-- 📷 图片 #4：终端运行 install_mac.sh 的成功输出 + 写入路径 -->
  <img src="docs/images/install-macos.png" alt="在终端运行 install_mac.sh" width="760">
</p>

**第二步 — 重启 Fusion 360**（完全退出再打开）。

**第三步 — 验证：** 打开螺纹命令，在「螺纹类型」下拉框里找到 `镜头尺寸螺纹规格`。完成 ✅

常用参数：

```bash
./install_mac.sh --dry-run                 # 只打印将要安装到哪个目录
./install_mac.sh --output /路径/ThreadData # 手动指定目录
```

### Windows

**第一步 — 运行安装脚本**（PowerShell）：

```powershell
powershell -ExecutionPolicy Bypass -File install_windows.ps1
```

> 如果 Windows 拦截脚本，上面命令里的 `-ExecutionPolicy Bypass` 已经针对这一次运行
> 放行了，你不需要更改任何系统设置。

<p align="center">
  <!-- 📷 图片 #5：PowerShell 运行 install_windows.ps1 的成功输出 + 目标路径 -->
  <img src="docs/images/install-windows.png" alt="在 PowerShell 运行 install_windows.ps1" width="760">
</p>

**第二步 — 重启 Fusion 360**（完全退出再打开）。

**第三步 — 验证：** 打开螺纹命令 →「螺纹类型」下拉框里已出现 `镜头尺寸螺纹规格`。完成 ✅

常用参数：

```powershell
powershell -ExecutionPolicy Bypass -File install_windows.ps1 -WhatIf
powershell -ExecutionPolicy Bypass -File install_windows.ps1 -OutputDir "C:\路径\ThreadData"
```

### 手动安装（任意系统）

若自动搜索失败（安装位置非标准），可手动复制成品 XML：

1. 从本仓库取 `LensSizeThreads.xml`。
2. 放进 Fusion 的 `ThreadData` 目录：
   - **macOS：**
     `~/Library/Application Support/Autodesk/Webdeploy/production/<版本ID>/Autodesk Fusion 360.app/Contents/Libraries/Applications/Fusion/Fusion/Server/Fusion/Configuration/ThreadData`
   - **Windows：**
     `%LOCALAPPDATA%\Autodesk\webdeploy\Production\<版本ID>\Fusion\Server\fusion\Configuration\ThreadData`
   - 有多个 `<版本ID>` 时选**最新**的那个。
3. 重启 Fusion 360。

<p align="center">
  <!-- 📷 图片 #10（可选）：文件管理器显示 ThreadData 目录里的 LensSizeThreads.xml -->
  <img src="docs/images/threaddata-folder.png" alt="LensSizeThreads.xml 放入 ThreadData 目录" width="760">
</p>

---

## 在 Fusion 360 中使用

**1. 先建一个圆柱**（或孔）用来加螺纹。

**2. 「创建 → 螺纹」。**

<p align="center">
  <!-- 📷 图片 #6：Fusion 功能区 创建 → 螺纹 高亮 -->
  <img src="docs/images/fusion-create-thread.png" alt="Fusion 360 功能区中的 创建 → 螺纹" width="640">
</p>

**3.** 勾选 **建模 (Modeled)**（让螺纹成为真实几何，而非仅贴图），
然后设置 **螺纹类型 → `镜头尺寸螺纹规格`**。

**4.** 选择 **尺寸 (Size)** 和 **规格 (Designation)**——如 M42 卡口选 `M42x1`，
42 mm 滤镜螺纹选 `M42x0.75`。

<p align="center">
  <!-- 📷 图片 #8：规格下拉框展开，显示 M42x1 / M42x0.75 / M39x1 ... -->
  <img src="docs/images/designation-list.png" alt="规格下拉框同时显示 1.0 mm 与 0.75 mm 两种螺距" width="560">
</p>

**5.** 若要做内螺纹（镜头拧入的环），再勾选 **内部 (Internal)**，点 **确定**。

<p align="center">
  <!-- 📷 图片 #7：完整螺纹对话框，勾选建模、选好族与规格，已应用到实体 -->
  <img src="docs/images/fusion-thread-dialog.png" alt="应用到实体上的完整螺纹对话框" width="820">
</p>

> **要让两个零件互相拧合**，给外螺件和内螺件选**同一尺寸、同一螺距**（如都为
> `M42x1`）。0.10 mm 配合间隙已内置，无需再改就能拧到一起。

<p align="center">
  <!-- 📷 图片 #9：两个打印件拧合在一起的照片 / 渲染 -->
  <img src="docs/images/result-part.png" alt="两个打印件拧合在一起" width="720">
</p>

---

## Fusion 更新之后

Fusion 360 每次大版本更新都会生成**新的** `ThreadData` 版本目录，自定义 XML **不会**
自动迁移。更新后只需**重新运行一次安装脚本**（脚本会指向最新版本目录）。也可使用社区
插件 [ThreadKeeper](https://github.com/thomasa88/ThreadKeeper) 在每次更新后自动重装。

## 常见问题

| 现象 | 解决办法 |
|------|----------|
| 看不到 `镜头尺寸螺纹规格` | 是否**完全重启**了 Fusion 360？自定义螺纹在启动时加载。 |
| 之前有、后来消失了 | Fusion 更新了 → 新版本目录。**重新运行安装脚本。** |
| 提示找不到 ThreadData | 用 `--output` / `-OutputDir` 手动指定目录，或走[手动安装](#手动安装任意系统)。 |
| Windows 提示"禁止运行脚本" | 用上面带 `-ExecutionPolicy Bypass` 的完整命令。 |
| 两个零件拧不到一起 | 确认两件用**同尺寸 + 同螺距**；一件内螺、一件外螺。 |
| 需要列表里没有的尺寸 / 螺距 | 见[二次开发](#二次开发--测试)，改一行即可。 |

## 原理

生成的 XML 遵循基本 **ISO 米制 60° 牙型**：

- `H = (√3 / 2) × 螺距`
- 中径 `d2 = d − 0.75·H`
- 小径 `d1 = d − 1.25·H`

外螺纹按 `0.10 mm` 间隙缩小、内螺纹放大同样量，因此同尺寸的内外螺纹能以轻微、
适合打印的间隙配合。详细算法与 Fusion XML 结构
（`<ThreadType> → <ThreadSize> → <Designation> → <Thread>`）见 `generate_lens_threads.py`。

## 二次开发 / 测试

改 `generate_lens_threads.py` 顶部两个列表即可增删尺寸 / 螺距：

```python
SIZES   = [24, 25, 25.5, ...]   # 公称直径 (mm)
PITCHES = [0.75, 1.0]           # 螺距 (mm)
```

重新生成并校验（需 Python 3.8+）：

```bash
python generate_lens_threads.py          # 生成 LensSizeThreads.xml
python tests/test_threads.py             # 校验 尺寸/螺距/内外螺/直径
python tests/compare_outputs.py \
    LensSizeThreads.xml \
    <mac_output>/LensSizeThreads.xml \
    <win_output>/LensSizeThreads.xml     # 校验三个生成器产物一致
```

bash 与 PowerShell 安装脚本内联了同一套生成逻辑，由 `compare_outputs.py` 保证三份
实现逐字节一致。

### 项目结构

```
fusion-lens-threads/
├── install_mac.sh            # macOS 安装脚本（自动搜索路径 + 生成 + 写入）
├── install_windows.ps1       # Windows 安装脚本（同上，PowerShell，无 BOM 的 UTF-8）
├── generate_lens_threads.py  # Python 生成器（跨平台，便于二次开发）
├── LensSizeThreads.xml       # 已生成的成品，可直接手动复制
├── tests/
│   ├── test_threads.py       # 结构 / 几何校验
│   └── compare_outputs.py    # 三个生成器一致性校验
├── docs/images/              # README 图片（含需补充的截图清单）
├── README.md                 # 英文说明
├── README.zh-CN.md           # 本文件（中文）
├── REDDIT.md                 # Reddit 发布 / 分享指南
└── LICENSE                   # MIT
```

## 参与贡献

欢迎提 Issue 和 PR，尤其是：

- 更多镜头 / 滤镜尺寸或非标准螺距，
- Linux 路径检测，
- 实际打印 / 装配的照片用于展示。

提 PR 前请先跑上面的测试，保证三个生成器同步。

## 开源协议

采用 **MIT License**（SPDX 标识符：[`MIT`](https://spdx.org/licenses/MIT.html)），
完整条款见 [`LICENSE`](LICENSE)。

MIT 协议本身**没有版本号**——只有唯一的一份标准文本，所以写「MIT」即可完整指明。
简言之：可自由使用、复制、修改、合并、发布、分发、再授权与出售，只需保留版权与许可
声明；软件按**原样 (as is)** 提供，不含任何担保。

```
SPDX-License-Identifier: MIT
Copyright (c) 2026 HairuoLiu
```

## 致谢

- 社区整理的 Fusion 360 自定义螺纹 XML 格式
  （含 [Nightkurz/CustomThreads](https://github.com/Nightkurz/CustomThreads)）。
- [ThreadKeeper](https://github.com/thomasa88/ThreadKeeper) 提供的"更新后自动重装"思路。

---

<p align="center">
  <sub>献给凌晨两点还在打印镜头转接环的人 · 想发到 Reddit？见 <a href="REDDIT.md">REDDIT.md</a>。</sub>
</p>
