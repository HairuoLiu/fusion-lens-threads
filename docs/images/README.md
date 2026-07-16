# Image manifest / 图片清单

This folder holds every image used by the README. Two of them are already
provided as ready-to-render SVGs. The rest are **screenshots you take yourself**
— just save each file with the exact name below and it will appear in the README
automatically (no Markdown editing needed).

本文件夹存放 README 用到的所有图片。其中两张已做好（SVG，GitHub 可直接渲染），
其余是**需要你自己截图**的：只要按下面的文件名保存到本目录，README 里对应位置就会
自动显示，无需改动 Markdown。

| # | Filename | Status | What it should show / 这张图要拍什么 | Suggested size |
|---|----------|--------|--------------------------------------|----------------|
| 1 | `banner.svg` | ✅ Provided | Hero banner (title + lens motif). | 1280×440 |
| 2 | `thread-geometry.svg` | ✅ Provided | ISO 60° thread profile explainer. | 900×440 |
| 3 | `thread-type-dropdown.png` | ⬜ **You capture** | **The money shot.** Fusion 360 Thread dialog with the *Thread Type* dropdown open, showing **镜头尺寸螺纹规格** highlighted in the list. | ~1000 px wide |
| 4 | `install-macos.png` | ⬜ You capture | Terminal after running `./install_mac.sh`, showing the green success line + the path it wrote to. | ~900 px wide |
| 5 | `install-windows.png` | ⬜ You capture | PowerShell after running `install_windows.ps1`, showing the success message + target path. | ~900 px wide |
| 6 | `fusion-create-thread.png` | ⬜ You capture | Fusion ribbon: **Create → Thread** menu item highlighted (or the Thread dialog first opening). | ~800 px wide |
| 7 | `fusion-thread-dialog.png` | ⬜ You capture | Full Thread dialog with **Modeled** checked, Thread Type = 镜头尺寸螺纹规格, a Size + Designation chosen (e.g. `M42x1`), applied to a cylinder in the canvas. | ~1100 px wide |
| 8 | `designation-list.png` | ⬜ You capture | The *Designation* dropdown open, showing entries like `M42x1`, `M42x0.75`, `M39x1` … so people see both pitches exist. | ~700 px wide |
| 9 | `result-part.png` | ⬜ You capture | Photo (or render) of two printed/machined parts screwed together — e.g. a lens barrel threaded into a filter ring. Proof it actually fits. | ~1000 px wide |
| 10 | `threaddata-folder.png` | ⬜ Optional | File Explorer / Finder showing the `ThreadData` folder with `LensSizeThreads.xml` sitting inside it. Helps people who install manually. | ~900 px wide |

## Tips for good screenshots / 截图小贴士

- Use a clean Fusion 360 theme (default dark is fine) and crop tightly to the
  dialog — remove desktop clutter.
- PNG for screenshots, keep each file under ~500 KB (resize to the width above).
- On macOS: `Cmd+Shift+4` then drag; on Windows: `Win+Shift+S`.
- For #9, good lighting + a plain background makes it look professional on Reddit.
- Optional: record a 5–10 s screen GIF of picking the thread and name it
  `demo.gif`; then add `![demo](docs/images/demo.gif)` near the top of the README.
