# Camera Lens and Filter Threads — v1.2.0

Adds the **Leica Thread Mount (L39 / LTM)** — the one photographic mount whose
pitch is neither 0.75 mm nor 1.0 mm.

## What's new

- **`M39x1/26-LTM`** in the `Camera Lens and Filter Threads` family:
  39 mm × **26 TPI = 25.4 / 26 = 0.976923 mm** on the standard 60° profile.
  Previously the 39 mm entry only offered 0.75 mm and 1.0 mm, neither of which
  is the real Leica screw mount.
- **New family `Leica Thread Mount (L39/LTM)`** (file `LensMountThreads.xml`):
  the same 26 TPI pitch with the historically correct **Whitworth 55°** flank
  angle and Whitworth depths (`d₂ = d − 0.640327·P`, `d₁ = d − 1.280655·P`).
- Installers now write **two** XML files into every detected `ThreadData`
  folder (`LensSizeThreads.xml` + `LensMountThreads.xml`).
- Pitch values are emitted with 6 decimals, so imperial-derived pitches such as
  26 TPI keep full precision (was rounded to 0.9769 at 4 decimals).
- Test harness extended: `tests/test_threads.py` now validates both families,
  including the exact 26 TPI pitch and the Whitworth diameters;
  `tests/compare_outputs.py` can compare both files across all three
  generators (Python / bash / PowerShell).
- App Store add-in (`LensSizeThreads.bundle`) updated to install both families.

## Why 0.976923 mm and not 1.0 mm

The LTM was standardised at **26 threads per inch** because Leitz inherited
Whitworth tooling from its microscope production (RMS thread). Three different
mounts share the "39 mm" number:

| Mount | Pitch | TPI | Flange focus |
|---|---|---|---|
| **L39 / LTM** (true Leica screw mount) | 0.976923 mm | 26 | 28.8 mm |
| M39 (Zenit / enlarger) | 1.0 mm | 25.4 | 45.2 / 28.8 mm |
| Canon J-mount | 1.058 mm | 24 | 28.8 mm |

A 1.0 mm adapter does not correctly mate with a true LTM lens.

## Which entry should I use?

- **3D printing an adapter** → `Camera Lens and Filter Threads` →
  `M39x1/26-LTM` (60°). The profile difference vs 55° is ~0.02 mm on the pitch
  diameter and is absorbed by the built-in 0.10 mm clearance.
- **Historically correct geometry / machining** → `Leica Thread Mount (L39/LTM)`
  → `M39x1/26` (Whitworth 55°).

Flange focal distance (28.8 mm for LTM) is a body/lens dimension, not a thread
dimension — set it in your model.

## Install

```bash
# macOS
./install_mac.sh

# Windows (PowerShell)
powershell -ExecutionPolicy Bypass -File install_windows.ps1
```

Restart Fusion 360, then *Create › Thread* → pick either family.

## Notes

- Fusion creates a new `ThreadData` version folder on every major update and
  does **not** migrate custom XML — re-run the installer after updating.
- Files changed: `generate_lens_threads.py`, `install_windows.ps1`,
  `install_mac.sh`, `LensSizeThreads.xml`, `LensMountThreads.xml` (new),
  `tests/*`, `LensSizeThreads.bundle/**`, both READMEs.

MIT — see `LICENSE`. SPDX: `MIT`.
