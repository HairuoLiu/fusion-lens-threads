# 图片清单 / Image manifest

This folder holds every image used by the README. Two are already provided as
ready-to-render SVGs (`banner.svg`, `thread-geometry.svg`). The rest are
screenshots **you take yourself** — save each with the exact filename below and
it appears in the README automatically (no Markdown editing needed).

本文件夹是 README 用到的所有图片。其中两张已做好（SVG，`banner.svg`、
`thread-geometry.svg`）。其余需要你按下面的**文件名**截图保存，README 对应位置
会自动显示，无需改 Markdown。

## 总表 / Overview

| # | 文件名 | 状态 | 内容 / What it shows | 建议尺寸 |
|---|--------|------|----------------------|-----------|
| 1 | `banner.svg` | ✅ 已提供 | 题头横幅（标题 + 镜头元素） | 1280×440 |
| 2 | `thread-geometry.svg` | ✅ 已提供 | ISO 60° 牙型讲解图 | 900×440 |
| 3 | `thread-type-dropdown.png` | ⬜ 你来拍 | **最关键的一张。** Fusion 螺纹对话框，「螺纹类型」下拉展开，显示并高亮「Camera Lens and Filter Threads」 | 约 1000px 宽 |
| 4 | `install-macos.png` | ⬜ 你来拍 | 终端运行 `./install_mac.sh` 后的成功输出 + 写入路径 | 约 900px 宽 |
| 5 | `install-windows.png` | ⬜ 你来拍 | PowerShell 运行 `install_windows.ps1` 后的成功信息 + 目标路径 | 约 900px 宽 |
| 6 | `fusion-create-thread.png` | ⬜ 你来拍 | Fusion 功能区「创建 → 螺纹」高亮 | 约 800px 宽 |
| 7 | `fusion-thread-dialog.png` | ⬜ 你来拍 | 完整螺纹对话框：勾选「建模」、螺纹类型已选、尺寸+规格已选（如 M42x1），已应用到画布上的圆柱 | 约 1100px 宽 |
| 8 | `designation-list.png` | ⬜ 你来拍 | 「规格」下拉展开，显示 M42x1 / M42x0.75 / M39x1… 两种螺距都在 | 约 700px 宽 |
| 9 | `result-part.png` | ⬜ 你来拍 | 两个打印件拧合在一起的照片/渲染（如镜头拧入滤镜环） | 约 1000px 宽 |
| 10 | `threaddata-folder.png` | ⬜ 可选 | 文件管理器显示 ThreadData 目录里已有 LensSizeThreads.xml | 约 900px 宽 |

---

## 每张图怎么拍 / How to capture each

### #3 `thread-type-dropdown.png` —— 最重要的"证据图"
**要拍成什么样：** Fusion 360 的螺纹对话框，"Thread Type / 螺纹类型"那个下拉框是**展开**的，列表里能清楚看到 **`Camera Lens and Filter Threads`** 这一项（建议把它选中/高亮，和内置的 ANSI/ISO 那一堆线程族并列）。
**步骤：**
1. 打开 Fusion 360（已装好本库并重启过）。
2. 建一个圆柱（任意尺寸，比如直径 42mm、长 10mm）。
3. 菜单 `创建 → 螺纹`。
4. 在弹出的对话框里，点开「螺纹类型」下拉（默认可能是 "ANSI Inch" / "ISO Metric"）。
5. 往下找，直到看到 **Camera Lens and Filter Threads**，点它选中（或保持下拉展开露出名字）。
6. 只截对话框这一块，保存为 `thread-type-dropdown.png`。
> 这张是 Reddit 上最容易吸赞的图，务必拍清楚。

### #4 `install-macos.png`
**要拍成什么样：** 终端窗口，能看到你跑的两条命令（`chmod +x install_mac.sh`、`./install_mac.sh`），以及成功行：`Installed LensSizeThreads.xml to: /Users/.../ThreadData` 和 `Restart Fusion 360...`。
**步骤：** 打开"终端"，`cd` 进项目文件夹，依次运行 README macOS 第一步的命令，截下成功输出。

### #5 `install-windows.png`
**要拍成什么样：** 蓝色 PowerShell 窗口，显示运行 `install_windows.ps1` 后的成功信息 + 目标路径（如 `...\webdeploy\Production\<版本>\...\ThreadData`）。
**步骤：** 打开 PowerShell，`cd` 进项目文件夹，运行 README Windows 第一步命令，截下输出。

### #6 `fusion-create-thread.png`
**要拍成什么样：** Fusion 顶部功能区，"创建 (Create)" 选项卡下的「螺纹 (Thread)」命令被高亮（或螺纹对话框刚弹出的样子）。
**步骤：** 在建模工作区，点开"创建"菜单，把鼠标悬停/点选「螺纹」，截功能区这一块。

### #7 `fusion-thread-dialog.png`
**要拍成什么样：** 完整的螺纹对话框：已勾「建模 (Modeled)」、螺纹类型 = Camera Lens and Filter Threads、尺寸和规格已选（例如 尺寸 42、规格 `M42x1`）、画布上能看到带螺纹的圆柱。
**步骤：** 选好螺纹类型后，选 尺寸 42、规格 `M42x1`，勾「建模」；点「确定」前先截图（这样设置都看得见），背景画布留着圆柱。

### #8 `designation-list.png`
**要拍成什么样：** 「规格 (Designation)」下拉展开，能同时看到 `M42x1`、`M42x0.75`、`M39x1` 等多项——让人一眼看到**两种螺距都存在**。
**步骤：** 在螺纹对话框里选好螺纹类型后，点开「规格」下拉，截下图，确保同一个尺寸下 x1 和 x0.75 都露出来。

### #9 `result-part.png`
**要拍成什么样：** 两个 3D 打印件拧在一起的照片或渲染（例如一个镜头筒拧进一个滤镜环，或转接环拧到镜头上），清楚看得出能拧合。
**步骤：** 用本库打印一对"外螺+内螺"件（同尺寸同螺距，如 M42x1），拧到一起，在干净背景、光线好的地方拍照；或用渲染图。
> Reddit 上"实物能拧上"的图可信度最高。

### #10 `threaddata-folder.png`（可选）
**要拍成什么样：** 文件管理器（资源管理器/Finder）打开 ThreadData 文件夹，里面能看到 `LensSizeThreads.xml`（和其他 Fusion 线程 XML 并列）。
**步骤：** 按 README 手动安装路径导航过去，截文件夹内容。

---

## 截图小贴士 / Tips
- 用干净的 Fusion 主题（默认深色即可），紧贴对话框裁切，去掉桌面杂物。
- 截图用 PNG，单张控制在 ~500KB 以内（按上面宽度缩放）。
- macOS 截图：`Cmd+Shift+4` 拖选；Windows：`Win+Shift+S`。
- #9 光线好 + 纯色背景，在 Reddit 上更显专业。
- 可选：录一段 5–10 秒"选螺纹并命名"的屏幕 GIF，命名为 `demo.gif`，在 README 顶部加 `![demo](docs/images/demo.gif)`。
