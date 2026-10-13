<!-- Language switch -->
**English** · [简体中文](README.zh-CN.md)

<p align="center">
  <img src="docs/images/banner.svg" alt="fusion-lens-threads — custom camera-lens & filter threads for Autodesk Fusion 360" width="100%">
</p>

<p align="center">
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg"></a>
  <img alt="Platform" src="https://img.shields.io/badge/platform-macOS%20%7C%20Windows-blue">
  <img alt="Dependencies" src="https://img.shields.io/badge/runtime%20deps-none-brightgreen">
  <img alt="Fusion 360" src="https://img.shields.io/badge/Autodesk-Fusion%20360-orange">
  <img alt="Threads" src="https://img.shields.io/badge/threads-73%20sizes%20%C3%97%202%20pitches%20%2B%20L39%2FLTM-9cf">
  <a href="https://apps.autodesk.com/FUSION/en/Detail/Index?id=4331085586591467927"><img alt="Autodesk App Store" src="https://img.shields.io/badge/Autodesk-App%20Store-orange"></a>
  <a href="#contributing"><img alt="PRs welcome" src="https://img.shields.io/badge/PRs-welcome-success"></a>
</p>

<p align="center">
  <a href="https://apps.autodesk.com/FUSION/en/Detail/Index?id=4331085586591467927">
    <img src="https://img.shields.io/badge/Install%20from-Autodesk%20App%20Store-blue?logo=autodesk&logoColor=white" alt="Install from the Autodesk App Store"></a>
</p>

> 🟠 **Now listed on the Autodesk App Store!** The easiest install: in Fusion 360
> open *Scripts and Add-Ins* → *App Store*, search **Camera Lens and Filter
> Threads**, and click **Install**. *(Store page is in review; the link goes live
> for everyone once Autodesk approves it.)*

> A one-click custom thread library that adds **every common camera-lens and
> filter thread** (M39, M40, M42, M43 … up to 127 mm) to Autodesk Fusion 360 —
> each in **both 0.75 mm and 1.0 mm pitch**, with proper clearance so parts
> actually screw together. It also adds the **true Leica Thread Mount —
> L39 / LTM, 39 mm × 26 TPI (0.976923 mm)**, which is neither 0.75 nor 1.0 mm.
> macOS & Windows installers, zero runtime dependencies.

<p align="center">
  <!-- 📷 IMAGE #3 (the money shot): Fusion Thread dialog with the Thread Type
       dropdown open, showing "Camera Lens and Filter Threads" highlighted. See docs/images/README.md -->
  <img src="docs/images/thread-type-dropdown.png" alt="The 'Camera Lens and Filter Threads' family appears in Fusion 360's Thread Type dropdown" width="720">
  <br><em>After installing, the <strong>Camera Lens and Filter Threads</strong> family shows up right in the Thread command.</em>
</p>

---

## Table of contents

- [Why this exists](#why-this-exists)
- [Features](#features)
- [Supported sizes & pitches](#supported-sizes--pitches)
- [Which pitch: 0.75 vs 1.0 mm](#which-pitch-075-vs-10-mm)
- [Requirements](#requirements)
- [Installation](#installation)
  - [From the Autodesk App Store (easiest)](#from-the-autodesk-app-store-easiest)
  - [macOS](#macos)
  - [Windows](#windows)
  - [Manual install (any OS)](#manual-install-any-os)
- [Using it in Fusion 360](#using-it-in-fusion-360)
- [After a Fusion 360 update](#after-a-fusion-360-update)
- [Troubleshooting](#troubleshooting)
- [How it works](#how-it-works)
- [Customizing / development](#customizing--development)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## Why this exists

Fusion 360 ships with standard ISO / UTS thread tables, but **photographic lens
and filter threads are not in there** — things like the M42 lens mount, M39
(Leica screw mount), or the dozens of filter-ring diameters (49 mm, 52 mm,
77 mm …). If you 3D-print or machine lens adapters, filter rings, step-up rings,
or custom mounts, you normally have to hand-model each thread.

This project drops a ready-made thread family into Fusion so you can just pick
the size and pitch from the dropdown — like any built-in thread.

## Features

- 🔍 **Auto-detects** your Fusion 360 `ThreadData` folder (newest installed
  version) on macOS and Windows — no hunting through hidden app folders.
- 📦 **73 diameters** covering the full common lens/filter range (24 – 127 mm).
- 🎯 **Two pitches per size** — `0.75 mm` and `1.0 mm` (e.g. `M42x1` mount and
  `M42x0.75` filter thread).
- 🎞 **Leica Thread Mount (L39 / LTM)** — the real mount is **26 TPI =
  0.976923 mm**, not 1.0 mm. Available as `L39x1/26-LTM` in the main family
  (60° profile) and as `L39x1/26` in a second family with the historically
  correct **Whitworth 55°** flank angle.
- 🔩 **External (6g) + internal (6H)** for every entry, with a 0.10 mm fit
  clearance so an external thread screws into an internal one of the same size.
- 🪶 **Zero runtime dependencies** — macOS uses the built-in `bash`, Windows uses
  the built-in `PowerShell`. No Python required to install.
- 🧪 **Tested** — a Python generator + test harness verify all three generators
  (Python / bash / PowerShell) produce identical, valid Fusion XML.
- 🛠️ **Hackable** — change one list to add your own sizes or pitches.

## Supported sizes & pitches

All diameters (mm), each available in **0.75 mm** and **1.0 mm** pitch:

```
24    25    25.5  27    28    30    30.5  34    35.5  36    36.5  37    37.5
38.5  39    40    40.5  41    42    43    43.5  44    46    46.5  48    49
50    50.5  52    54    55    56    58    60    62    64    67    70    72
74    75    76    77    78    80    82    84    85    86    87    90    92
94    95    96    98    100   102   104   105   107   108   110   112   114
116   118   120   122   124   125   126   127
```

That's **73 sizes × 2 pitches × (external + internal) = 292 thread definitions**.
The commonly requested `M39`, `M40`, `M42`, `M43` are all included.

### The oddball: Leica Thread Mount (L39 / LTM)

Photographic filter threads are metric, but the **Leica Thread Mount is not**:

| Mount | Diameter | Pitch | TPI | Flange focus |
|---|---|---|---|---|
| **L39 / LTM** (Leica screw mount) | 39 mm | **0.976923 mm** | 26 | 28.8 mm |
| M39 (Soviet/Zenit, enlarger) | 39 mm | 1.0 mm | 25.4 | 45.2 / 28.8 mm |
| Canon J-mount | 39 mm | 1.058 mm | 24 | 28.8 mm |

**`L39` = `LTM` = `LSM` — three names, one mount.** They all mean exactly this:
39 mm × 26 TPI. "M39" is the popular nickname (it is the title of the Wikipedia
article), but it is **ambiguous**: a true metric **M39×1** (Zenit SLR / enlarger
thread, 1.0 mm) is a *different* thread, and mixing them is the single most
common way to build a 39 mm adapter that will not focus. That is why the
designation here is prefixed **`L39`**, not `M39` — while `M39×1` remains
available in the standard family for the Soviet/enlarger mount.

`0.976923 mm = 25.4 mm / 26`. Both LTM families here use that exact pitch:

- **`Camera Lens and Filter Threads` → `L39x1/26-LTM`** — 26 TPI pitch on a
  standard 60° profile. This is the pragmatic choice for 3D-printed adapters
  (most published LTM adapters are modelled at 60°, and the 0.10 mm clearance
  absorbs the profile difference).
- **`Leica Thread Mount (L39/LTM)` → `L39x1/26`** — the same pitch with the
  original **Whitworth 55°** flank angle and Whitworth depths
  (`d₂ = d − 0.640327·P`, `d₁ = d − 1.280655·P`). Use this when you want the
  historically correct form.

Flange focal distance (28.8 mm for LTM) is a body/lens dimension, not a thread
dimension — set it in your model, the thread file only defines the thread.

## Which pitch should I use? 0.75 mm vs 1.0 mm

Both pitches exist for a reason: **the same diameter number can be a filter
thread (0.75 mm) or a lens mount (1.0 mm)** — the pitch is what tells them
apart.

**Quick rule**
- **0.75 mm** → the thread on the *front of a lens* (where you screw
  UV/ND/CPL filters, lens caps, hoods, step-up rings). This is the
  photographic standard for filter threads up to ~86 mm.
- **1.0 mm** → (a) **large filter diameters** (95, 105, 112, 120, 127 mm),
  and (b) **screw lens mounts** like `M42×1` (Pentax/Praktica SLR) and
  `M39×1` (Leica Thread Mount rangefinder).

| You are modeling… | Use | Examples |
|---|---|---|
| A screw-in filter, cap, hood, or filter step-ring (≤ 86 mm) | **0.75 mm** | 49, 52, 67, 77 mm filter threads |
| A large filter accessory (≥ 95 mm) | **1.0 mm** | 95, 105, 112, 120, 127 mm |
| An adapter to a vintage **M42** screw-mount lens | **1.0 mm** | `M42×1` (Pentax/Praktica) |
| An adapter to a **Leica** screw-mount lens (L39/LTM) | **26 TPI = 0.976923 mm** | `L39x1/26-LTM` |
| Unsure / generic filter part | default to **0.75 mm** | safe choice |

**Concrete size notes (the ones people mix up)**
- **M39** (three different things share this number — check the pitch):
  - `M39×0.75` → a 39 mm **filter thread**.
  - `M39×1.0` → Soviet **Zenit M39** / enlarger M39 (a DIN 1 mm thread).
  - `L39x1/26-LTM` → the real **Leica Thread Mount**, **26 TPI = 0.976923 mm**.
    Leitz used a Whitworth-form thread because the plant already made
    microscopes (RMS thread), which is why the pitch is not a round metric
    number. A 1.0 mm adapter will *not* correctly mate with a true LTM lens.
- **M40 / 40.5**: filter threads → `0.75 mm`.
- **M42**: `M42×0.75` = 42 mm filter thread; `M42×1.0` = the famous SLR
  screw mount (use 1.0 for adapters).
- **M43**: filter thread → `0.75 mm`.

In Fusion 360, just pick the matching designation in the *Designation* dropdown
— the screenshot below shows both pitches listed side by side.

<p align="center">
  <img src="docs/images/thread-geometry.svg" alt="ISO metric 60-degree thread profile with pitch, major/minor diameter and fit clearance" width="720">
</p>

<p align="center">
  <img src="docs/images/designation-list.png" alt="Fusion 360 Designation dropdown showing M46x0.75 and M46x1.0 side by side" width="560">
  <br><em>The <strong>Designation</strong> dropdown lists both pitches for each size — e.g. <code>M46x0.75</code> (filter) and <code>M46x1.0</code> (mount).</em>
</p>

## Requirements

- Autodesk Fusion 360 (any recent version) installed.
- macOS **or** Windows. No Python, no plugins, no admin rights needed for the
  default install.

---

## Installation

> **TL;DR:** run one script → **restart Fusion 360** → pick
> `Camera Lens and Filter Threads` in the Thread dialog. Three steps, done.

### From the Autodesk App Store (easiest)

1. In Fusion 360, open **Scripts and Add-Ins** (under the *Tools* menu), then click
   the **App Store** tab (or the store icon).
2. Search for **Camera Lens and Filter Threads** and click **Install**.
3. The add-in copies the thread library into Fusion's configuration and prompts you
   to **restart Fusion 360**. After restart, the family appears in the Thread Type
   dropdown.

You can also open the store page directly:
**https://apps.autodesk.com/FUSION/en/Detail/Index?id=4331085586591467927**

> Prefer the manual route? The sections below show how to install from this repo
> with the included scripts.

First, get the files — either **clone** or **download the ZIP** from the green
`Code` button on GitHub and unzip it:

```bash
git clone https://github.com/HairuoLiu/fusion-lens-threads.git
cd fusion-lens-threads
```

### macOS

**Step 1 — Run the installer**

```bash
chmod +x install_mac.sh
./install_mac.sh
```

The script finds your Fusion `ThreadData` folder automatically and writes both
thread files into it: `LensSizeThreads.xml` (filters + `L39x1/26-LTM`) and
`LensMountThreads.xml` (L39/LTM, Whitworth 55°).

**Step 2 — Restart Fusion 360** (fully quit and reopen).

**Step 3 — Verify:** open the Thread command and look for `Camera Lens and Filter Threads`
and `Leica Thread Mount (L39/LTM)` in the Thread Type dropdown. Done ✅

Handy flags:

```bash
./install_mac.sh --dry-run                 # just print where it WOULD install
./install_mac.sh --output /path/ThreadData # install to a specific folder
```

### Windows

**Step 1 — Run the installer** (PowerShell):

```powershell
powershell -ExecutionPolicy Bypass -File install_windows.ps1
```

> If Windows blocks the script, the `-ExecutionPolicy Bypass` flag above already
> handles it for this one run — you don't need to change any system settings.

<p align="center">
  <!-- 📷 IMAGE #5: PowerShell showing install_windows.ps1 success output + target path -->
  <img src="docs/images/install-windows.png" alt="Running install_windows.ps1 in PowerShell" width="760">
</p>

**Step 2 — Restart Fusion 360** (fully quit and reopen).

**Step 3 — Verify:** open the Thread command → the Thread Type dropdown now
lists `Camera Lens and Filter Threads` (with `L39x1/26-LTM` under Size 39) and
`Leica Thread Mount (L39/LTM)`. Done ✅

> The installer writes **two** files into every detected `ThreadData` folder:
> `LensSizeThreads.xml` and `LensMountThreads.xml`.

Handy flags:

```powershell
powershell -ExecutionPolicy Bypass -File install_windows.ps1 -WhatIf
powershell -ExecutionPolicy Bypass -File install_windows.ps1 -OutputDir "C:\path\to\ThreadData"
```

### Manual install (any OS)

If auto-detection fails (unusual install location), copy the pre-built XML
yourself:

1. Grab **both** `LensSizeThreads.xml` and `LensMountThreads.xml` from this repo.
2. Drop them into your Fusion `ThreadData` folder:
   - **macOS:**
     `~/Library/Application Support/Autodesk/Webdeploy/production/<version-id>/Autodesk Fusion 360.app/Contents/Libraries/Applications/Fusion/Fusion/Server/Fusion/Configuration/ThreadData`
   - **Windows:**
     `%LOCALAPPDATA%\Autodesk\webdeploy\Production\<version-id>\Fusion\Server\fusion\Configuration\ThreadData`
   - Pick the **newest** `<version-id>` folder if there are several.
3. Restart Fusion 360.

---

## Using it in Fusion 360

**1. Make a cylinder** (or a hole) to thread.

**2. `Create → Thread`.**

**3.** Tick **Modeled** (so the thread is real geometry, not just cosmetic), then
set **Thread Type → `Camera Lens and Filter Threads`**.

**4.** Choose **Size** and **Designation** — e.g. `M42x1` for an M42 mount, or
`M42x0.75` for a 42 mm filter thread.

**5.** For an internal thread (a ring the lens screws into), also tick
**Internal**. Click **OK**.

<p align="center">
  <img src="docs/images/fusion-create-thread.png" alt="Fusion 360 Create Thread dialog with Camera Lens and Filter Threads selected" width="820">
  <br><em>The <strong>Thread</strong> dialog with <strong>Camera Lens and Filter Threads</strong> selected — pick Size and Designation, then OK.</em>
</p>

<p align="center">
  <img src="docs/images/result-part.png" alt="Modeled thread result on a cylindrical part in Fusion 360" width="820">
  <br><em>The result: a fully modeled camera-lens thread on your part, ready for 3D printing or machining.</em>
</p>

> **To make two parts screw together**, give the external part and the internal
> part the **same size and pitch** (e.g. both `M42x1`). The 0.10 mm clearance is
> already built in, so they'll thread together without editing.

---

## After a Fusion 360 update

Every major Fusion update creates a **new** `ThreadData` version folder, and
custom XML is **not** migrated automatically. After an update, just **re-run the
installer** (it targets the newest version folder). You can also use the
community add-in [ThreadKeeper](https://github.com/thomasa88/ThreadKeeper) to
re-apply custom threads automatically after each update.

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| `Camera Lens and Filter Threads` doesn't appear | Did you fully **restart** Fusion 360? Custom threads load at startup. |
| It appeared before but vanished | Fusion updated → new version folder. **Re-run the installer.** |
| Installer says "ThreadData not found" | Use `--output` / `-OutputDir` to point at the folder manually, or do the [manual install](#manual-install-any-os). |
| Windows: "running scripts is disabled" | Use the exact command with `-ExecutionPolicy Bypass` shown above. |
| Parts don't screw together | Make sure both parts use the **same size *and* pitch**; only one is Internal, the other External. |
| I need a size/pitch that isn't listed | See [Customizing](#customizing--development) — it's one line. |

## How it works

The generated XML follows the basic **ISO metric 60° profile**:

- `H = (√3 / 2) × pitch`
- pitch diameter `d2 = d − 0.75·H`
- minor diameter `d1 = d − 1.25·H`

External threads are shrunk by a `0.10 mm` allowance and internal threads grown
by the same amount, so a same-size external/internal pair mates with a light,
printable clearance. See `generate_lens_threads.py` for the exact math and the
Fusion XML schema (`<ThreadType> → <ThreadSize> → <Designation> → <Thread>`).

The second family uses the **Whitworth 55°** form instead:

- `d₂ = d − 0.640327·P`
- `d₁ = d − 1.280655·P`

with `P = 25.4 / 26 = 0.976923 mm` for the L39 / LTM mount. Because Fusion
models threads from (major, pitch, minor) diameters plus the flank angle, a
55° family reproduces the historical LTM profile far better than a 60°
approximation — but for 3D printing the difference is ~0.02 mm on the pitch
diameter, so the 60° entry is usually good enough.

| | `Camera Lens and Filter Threads` | `Leica Thread Mount (L39/LTM)` |
|---|---|---|
| File | `LensSizeThreads.xml` | `LensMountThreads.xml` |
| Flank angle | 60° (ISO metric) | 55° (Whitworth) |
| Contents | 73 sizes × 0.75/1.0 mm + `L39x1/26-LTM` | `L39x1/26` (26 TPI) |
| Use for | filters, hoods, step rings, M42 adapters | true Leica screw-mount adapters |

## Customizing / development

Add or remove sizes/pitches by editing the lists at the top of
`generate_lens_threads.py`:

```python
SIZES   = [24, 25, 25.5, ...]   # nominal diameters in mm
PITCHES = [0.75, 1.0]           # pitches in mm

# Non-metric mounts: (size, designation label, pitch)
SPECIAL_DESIGNATIONS = [(39, "L39x1/26-LTM", 25.4 / 26.0)]

# Second family: Whitworth 55 deg mounts
LTM_SIZES = [(39, "L39x1/26", 25.4 / 26.0)]
```

Pitch values are printed with 6 decimals (`fmt_pitch`) so imperial-derived
pitches such as 26 TPI keep their precision:

```bash
python generate_lens_threads.py          # writes both XML files
python tests/test_threads.py             # validates sizes/pitches/genders/diameters
python tests/compare_outputs.py \
    LensSizeThreads.xml \
    <mac_output>/LensSizeThreads.xml \
    <win_output>/LensSizeThreads.xml     # confirms all 3 generators match
```

The bash and PowerShell installers embed the same generator inline, so the three
implementations are kept byte-for-byte identical by `compare_outputs.py`.

### Project structure

```
fusion-lens-threads/
├── install_mac.sh            # macOS installer (auto-detect path + generate + write)
├── install_windows.ps1       # Windows installer (same, PowerShell, UTF-8 no BOM)
├── generate_lens_threads.py  # Python generator (cross-platform, for tweaking)
├── LensSizeThreads.xml       # pre-built: filters + 0.75/1.0 mm + L39x1/26-LTM
├── LensMountThreads.xml      # pre-built: L39/LTM, Whitworth 55 deg, 26 TPI
├── tests/
│   ├── test_threads.py       # schema/geometry validation
│   └── compare_outputs.py    # cross-generator equality check
├── docs/images/              # README images (+ manifest of screenshots to add)
├── README.md                 # this file (English)
├── README.zh-CN.md           # 中文说明
├── REDDIT.md                 # launch/share guide for Reddit
└── LICENSE                   # MIT
```

## Automated Reddit posting (Reddit MCP connector)

Instead of copy-pasting by hand, WorkBuddy can post the launch announcements
for you through the **Reddit MCP connector**. This repo ships **12 ready-to-post
drafts** in [`reddit-posts/`](reddit-posts/README.md) — one per target
subreddit, each written to be unique (the server's safe-mode blocks identical
cross-subreddit content).

### 1. Get Reddit API credentials

The connector posts **as you**, so it needs a Reddit "script" app:

1. Go to <https://www.reddit.com/prefs/apps>.
2. Click **create app** → choose type **script** (not *web app* / *installed app*).
3. Name it anything (e.g. `fusion-lens-bot`); set `redirect uri` = `http://localhost`.
4. Copy what you get:
   - **client_id** — the id under the app name ("personal use script").
   - **client_secret** — the secret next to it.
   - your Reddit **username** and **password**.

### 2. Wire it into WorkBuddy

Add this server to your WorkBuddy `mcp.json` (usually
`~/.workbuddy/mcp.json`), filling in the four real values:

```json
{
  "mcpServers": {
    "reddit": {
      "command": "npx",
      "args": ["-y", "reddit-mcp-server"],
      "env": {
        "REDDIT_CLIENT_ID": "<your client_id>",
        "REDDIT_CLIENT_SECRET": "<your client_secret>",
        "REDDIT_USERNAME": "<your username>",
        "REDDIT_PASSWORD": "<your password>"
      },
      "disabled": false
    }
  }
}
```

> **Gotcha — `MCP error -32000: Connection closed`.**
> Do **not** leave the values as non-empty placeholders (e.g. `FILL_IN_*`):
> the server tries to authenticate with them, fails, and **exits**, which shows
> up as `Connection closed` in WorkBuddy. Use **real values** or **empty strings**
> (empty = anonymous read-only mode — connection stays up, but posting is blocked
> until you fill them in).

### 3. Trust & launch

1. Open **Connector management → custom connectors → reddit → Trust**.
2. Restart WorkBuddy (or toggle the connector off/on) so the tools load.
3. The agent can now call `mcp__reddit__create_post` / `reply_to_post` for each
   draft in `reddit-posts/`.

### Notes / safety

- Safe mode is **on by default**: ~2 s between writes and cross-subreddit
  duplicate detection, so the 12 drafts must stay unique (that's why there are
  12 files, not one copied 12×).
- Post **one Tier-1 sub per day**, not all at once, to avoid looking like spam.
  Engage with comments before the next post.
- Some subreddits require a **flair** or ban links in the body — check
  `get_subreddit_rules` / `get_post_flairs` first.
- See [`REDDIT.md`](REDDIT.md) for the full launch playbook (which subs, how to
  write, etiquette).

## Contributing

Issues and PRs are welcome — especially:

- extra lens/filter sizes or non-standard pitches,
- Linux path detection,
- real-world screenshots/prints for the gallery.

Please run the tests above before opening a PR so all three generators stay in
sync.

## License

Released under the **MIT License** (SPDX identifier: [`MIT`](https://spdx.org/licenses/MIT.html)).
See [`LICENSE`](LICENSE) for the full text.

The MIT License itself is unversioned — there is a single canonical text — so
"MIT" fully identifies it. In short: free to use, copy, modify, merge, publish,
distribute, sublicense, and sell, provided the copyright and permission notice
are kept. Provided **as is**, without warranty.

```
SPDX-License-Identifier: MIT
Copyright (c) 2026 HairuoLiu
```

## Acknowledgements

- The Fusion 360 custom-thread XML format, documented by the community
  (incl. [Nightkurz/CustomThreads](https://github.com/Nightkurz/CustomThreads)).
- [ThreadKeeper](https://github.com/thomasa88/ThreadKeeper) for the
  survive-updates workflow.

---

<p align="center">
  <sub>Made for people who print lens adapters at 2 a.m. · Sharing this on Reddit? See <a href="REDDIT.md">REDDIT.md</a>.</sub>
</p>
