# Autodesk App Store — Submission Pack

This folder is ready to submit to the **Autodesk App Store** (apps.autodesk.com →  
Fusion 360). Everything the Publisher Corner web form needs is prepared below.

> ⚠️ I (the agent) **cannot click "Submit" for you** — the Autodesk Publisher  
> Corner requires *your* Autodesk account login (SSO) and accepting the Publisher  
> Agreement. I have prepared every file and every text field. You do the final  
> upload + login.

---

## 1. What to upload

| Item                                        | File                                  | Status        |
| ------------------------------------------- | ------------------------------------- | ------------- |
| **App package (ZIP)**                       | `LensSizeThreads-AppStore-v1.1.0.zip` | ✅ built       |
| Icon 120×120 PNG                            | `appstore-icon-120x120.png`           | ✅ built       |
| Company logo 120×120 PNG                    | *reuse the icon*                      | ✅ (same file) |
| Screenshots (≤10, PNG/JPG, up to 2000×2000) | `docs/images/*.png` (5 usable)        | ✅ present     |

The package structure inside the ZIP:

```
LensSizeThreads.bundle/
├── PackageContents.xml            # App Store registration
└── Contents/
    ├── LensSizeThreads.Manifest    # Fusion add-in manifest
    ├── lens_thread_installer.py    # run() copies XML → Fusion ThreadData
    ├── LensSizeThreads.xml         # the 292-thread library
    ├── help.html                   # description / EULA info page
    ├── icon.png                    # 120×120
    ├── install_windows.ps1         # optional standalone installer
    ├── install_mac.sh              # optional standalone installer
    └── generate_lens_threads.py    # source generator
```

**Why a bundle/add-in?** The Autodesk autoloader only copies the bundle into  
`ApplicationPlugins`; it does **not** place files into Fusion's `ThreadData`  
folder. So we wrap the thread XML as a tiny Fusion Python add-in whose `run()`  
copies the XML into every detected ThreadData folder — satisfying the  
"ready to run, no manual copy" rule that pure config+script packages fail.

---

## 2. Web-form fields (copy-paste)

**Product type:** Desktop based app → **Add-in/Extension**  
**Autodesk Product Compatibility:** **Fusion 360**  *(the only compatible product — the
bundle's manifest declares `<AutodeskProduct>Fusion360</AutodeskProduct>` and uses the
`adsk.fusion` API, so do NOT select AutoCAD / Revit / Inventor / etc.)*  
**Supported OS:** Windows **and** Mac (submit/clone both)  
**Price:** **Free**  
**Version:** `1.1.0`  *(must increment on every future submission)*

**Title (≤100 chars):**

```
Camera Lens and Filter Threads
```

**Short description (≤100 chars):**

```
Add real camera lens & filter thread sizes (24–127 mm, 0.75/1.0 mm) to Fusion 360's Thread Type dropdown.
```

**App Description** *(HTML, ≤4000 chars — the long description box on the form.  
Paste as-is):*

```html
<h1>Camera Lens and Filter Threads for Fusion 360</h1>
<p>Free, open-source add-in that adds standard camera lens and filter thread
sizes to the <strong>Thread Type</strong> dropdown in Fusion 360 — so you can
model step-up rings, filter adapters, lens hoods, lens caps, and custom threaded
accessories with real, dimensionally correct threads.</p>

<h2>What you get</h2>
<ul>
  <li><strong>73 sizes</strong> from 24 mm to 127 mm — including 25, 30, 37, 39,
      40.5, 43, 46, 49, 52, 55, 58, 62, 67, 72, 77, 82, 86, 95, 105, 112, 127 mm.</li>
  <li><strong>Two pitches:</strong> 0.75 mm (used by almost all filter sizes) and
      1.0 mm (filters ≥95 mm, plus M39×1 and M42×1 lens mounts).</li>
  <li>Both <strong>male (external)</strong> and <strong>female (internal)</strong>
      threads — 292 thread definitions in total.</li>
</ul>

<h2>Why it helps</h2>
<p>Stock Fusion 360 only knows standard engineering threads (M, UNC/UNF, G, NPT…).
Camera and filter threads are a different world. This library closes that gap so
your 3D-printed adapters actually screw onto real lenses and filters.</p>

<h2>Open source</h2>
<p>MIT licensed. Source, generator, and docs:
<a href="https://github.com/HairuoLiu/fusion-lens-threads">github.com/HairuoLiu/fusion-lens-threads</a></p>
```

**General Usage Instructions** *(plain-text box on the form):*

```
```

**Installation/Uninstallation** *(plain-text box on the form):*

```
```

**Support Information** *(plain-text box on the form):*

```
```

**EULA:** leave the Autodesk standard EULA selected (free product). The MIT  
license + repo link are already stated in the description and in `help.html`  
(shipped inside the bundle), which satisfies the custom-terms disclosure.

---

## 3. Screenshots to upload (pick up to 10)

From `docs/images/` (all PNG, safe to use):

1. `thread-type-dropdown.png` — the Thread Type dropdown showing the entry
2. `fusion-create-thread.png` — the Create Thread dialog with the entry selected
3. `result-part.png` — the modeled thread result
4. `install-windows.png` — Windows install step
5. `designation-list.png` — the 0.75 / 1.0 mm pitch choice

(If Autodesk complains about PPI, open each in any editor and re-export at  
96 PPI; dimensions are already within the 2000×2000 limit.)

---

## 4. Step-by-step submission

1. Go to **<https://apps.autodesk.com>** → choose **Fusion 360**.
2. Scroll to the bottom → click **"Autodesk App Store developers!"** to open the  
   **Publisher Corner** (or go to <https://aps.autodesk.com/node/3040>).
3. Sign in with your **Autodesk account (SSO)** and accept the **Publisher  
   Agreement**. *(Free products do NOT require a PayPal account.)*
4. Click **"Submit a new app"** → choose **Desktop based app → Add-in/Extension**.
5. Fill the fields from section 2 (title, description, version `1.1.0`, Free).
6. Upload `LensSizeThreads-AppStore-v1.1.0.zip` as the **app package**.
7. Upload `appstore-icon-120x120.png` for **icon** and **logo**.
8. Upload the 5 screenshots from section 3.
9. Select **Windows** and **Mac** (clone the submission for the second OS if the  
   form only allows one per submission).
10. Submit. Review is typically **~24 h for the initial response, up to ~2 weeks**  
    for full approval. Autodesk's ADN team tests it and generates the final  
    installer (MSI/dmg) for you.

---

## 5. Rebuild / bump version

```bash
# after editing the thread library or add-in:
python build_appstore_bundle.py        # regenerates the .bundle + zip
# then update Version in build_appstore_bundle.py AND re-submit with a higher number
```

Official references:

- Publisher Corner: <https://aps.autodesk.com/node/3040>
- Fusion submission guide: <https://aps.autodesk.com/node/3050>
- Getting-started PDF: <https://damassets.autodesk.net/content/dam/autodesk/www/pdfs/app-store-getting-started-guide.pdf>
