# fusion-lens-threads

为 **Autodesk Fusion 360** 自动生成「镜头尺寸螺纹规格」自定义螺纹库，覆盖
所有常见镜头 / 滤镜螺纹直径（24 mm – 127 mm），并为每个尺寸同时提供
**0.75 mm** 与 **1.0 mm** 两种螺距，确保镜头能够顺利拧入（例如
M42×1 卡口、42 mm 滤镜螺纹等）。

安装后，在 Fusion 360 的「创建 > 螺纹」命令里，「螺纹类型 (Thread Type)」
下拉框中会出现 **镜头尺寸螺纹规格** 这一项。

---

## 特性

- 自动搜索 Fusion 360 的 `ThreadData` 目录（macOS / Windows 各预设多条候选路径，自动选最新版本号）。
- 一次性写入所有镜头螺纹尺寸，无需手动逐个添加。
- 每个尺寸都带 **外螺纹 (external / 6g)** 与 **内螺纹 (internal / 6H)**，
  并按 0.10 mm 的配合间隙计算，保证“外螺能拧进内螺”。
- 纯脚本、零运行时依赖：
  - macOS 用 `bash`（系统自带，无需 Python）。
  - Windows 用 `PowerShell`（系统自带，无需 Python）。
- 附带一个 Python 生成器 + 测试脚本，便于二次开发（改尺寸 / 改螺距）。

## 已覆盖的螺纹尺寸（共 73 个）

```
24  25  25.5  27  28  30  30.5  34  35.5  36  36.5  37  37.5  38.5
39  40  40.5  41  42  43  43.5  44  46  46.5  48  49  50  50.5
52  54  55  56  58  60  62  64  67  70  72  74  75  76  77  78
80  82  84  85  86  87  90  92  94  95  96  98  100 102 104 105
107 108 110 112 114 116 118 120 122 124 125 126 127   (单位：mm)
```

每个尺寸都提供两种螺距：**0.75 mm** 与 **1.0 mm**（对应如 `M42×0.75`、`M42×1`）。
用户点名要求的 39 / 40 / 42 / 43 等尺寸全部包含在内。

## 文件结构

```
fusion-lens-threads/
├── install_mac.sh          # macOS 安装脚本（自动搜索路径 + 生成 + 写入）
├── install_windows.ps1    # Windows 安装脚本（同上，PowerShell）
├── generate_lens_threads.py# Python 生成器（跨平台，便于二次开发）
├── LensSizeThreads.xml     # 已生成好的成品，可直接手动复制使用
├── tests/
│   ├── test_threads.py    # 校验 XML：尺寸/螺距/内外螺纹/直径合法性
│   └── compare_outputs.py # 校验三个生成器产物完全一致
├── README.md
└── LICENSE
```

---

## 安装

### macOS

```bash
chmod +x install_mac.sh
./install_mac.sh            # 自动搜索路径并安装
# 或只查看会装到哪个目录：
./install_mac.sh --dry-run
# 或手动指定 ThreadData 目录：
./install_mac.sh --output /path/to/ThreadData
```

### Windows (PowerShell)

```powershell
powershell -ExecutionPolicy Bypass -File install_windows.ps1
# 或只查看会装到哪个目录：
powershell -ExecutionPolicy Bypass -File install_windows.ps1 -WhatIf
# 或手动指定 ThreadData 目录：
powershell -ExecutionPolicy Bypass -File install_windows.ps1 -OutputDir "C:\path\to\ThreadData"
```

### 自动搜索的候选路径

脚本会在以下位置寻找带最新版本号的 `ThreadData` 目录，找到第一个即使用：

- **macOS**
  `~/Library/Application Support/Autodesk/Webdeploy/production/<版本ID>/Autodesk Fusion 360.app/Contents/Libraries/Applications/Fusion/Fusion/Server/Fusion/Configuration/ThreadData`
- **Windows**
  `%LOCALAPPDATA%\Autodesk\webdeploy\Production\<版本ID>\Fusion\Server\fusion\Configuration\ThreadData`

若自动搜索失败（例如 Fusion 装在非标准位置），可用 `--output` / `-OutputDir`
手动指向正确的 `ThreadData` 目录，或直接把仓库里的 `LensSizeThreads.xml` 复制进去。

---

## 在 Fusion 360 中使用

1. 运行对应平台的安装脚本。
2. **重启 Fusion 360**。
3. 「创建 > 螺纹」，勾选「建模 (Modeled)」。
4. 在「螺纹类型 (Thread Type)」里选择 **镜头尺寸螺纹规格**。
5. 在「规格 (Designation)」里挑选尺寸与螺距，例如：
   - `M42×1`（42 mm 卡口 / 1.0 mm 螺距，外螺用于镜头、内螺用于滤镜环）
   - `M42×0.75`（42 mm 滤镜螺纹 / 0.75 mm 螺距）
   - 同理适用于 39、43、52、77… 任意已覆盖尺寸。

> 小提示：要让两个零件互相拧合，请给“外螺件”和“内螺件”选用**同一个尺寸、
> 同一个螺距**（如都为 M42×1）。本库的几何已按配合间隙计算，可直接装配。

---

## Fusion 更新后

Fusion 360 每次大版本更新会生成新的 `ThreadData` 版本目录，自定义 XML 不会被自动迁移。
更新后只需**重新运行一次安装脚本**即可。也可使用社区插件
[ThreadKeeper](https://github.com/thomasa88/ThreadKeeper) 来自动重新安装。

---

## 二次开发 / 测试

修改 `generate_lens_threads.py` 顶部的 `SIZES` / `PITCHES` 即可增删尺寸或螺距，
重新运行 `python generate_lens_threads.py` 生成新的 `LensSizeThreads.xml`。

运行测试（需 Python 3.8+）：

```bash
python generate_lens_threads.py          # 生成 LensSizeThreads.xml
python tests/test_threads.py           # 校验 XML 是否符合规范
python tests/compare_outputs.py \
    LensSizeThreads.xml \
    <mac_output>/LensSizeThreads.xml \
    <win_output>/LensSizeThreads.xml   # 校验三个生成器产物完全一致
```

## 许可证

[MIT](LICENSE) — 自由使用、修改、再分发。
