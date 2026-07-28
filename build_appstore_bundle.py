"""Build the Autodesk App Store (.bundle) package for fusion-lens-threads.

Output:
  LensSizeThreads.bundle/            (ready-to-submit add-in bundle)
  LensSizeThreads-AppStore-v1.1.0.zip (the file you upload to Publisher Corner)

Why a bundle/add-in? The Autodesk App Store autoloader only copies the bundle
into ApplicationPlugins; it does NOT place files into Fusion's ThreadData folder.
So we wrap the thread XML as a tiny Fusion Python add-in whose run() copies the
XML into every detected ThreadData folder -- satisfying the "ready to run" rule.
"""
import os
import shutil
import struct
import zlib
import zipfile

ROOT = os.path.dirname(os.path.abspath(__file__))
VERSION = "1.1.0"
PRODUCT_CODE = "4C9CEE75-415B-4B3C-82B2-B91EFB0234DF"
UPGRADE_CODE = "46B1A8BF-D84F-46BD-AD21-98AAD311C861"
BUNDLE = os.path.join(ROOT, "LensSizeThreads.bundle")
CONTENTS = os.path.join(BUNDLE, "Contents")
APP_ZIP = os.path.join(ROOT, f"LensSizeThreads-AppStore-v{VERSION}.zip")

# --------------------------------------------------------------------------
# 1. The add-in that installs the thread XML into Fusion's ThreadData folder
# --------------------------------------------------------------------------
ADDIN_PY = '''import adsk.core, adsk.fusion, traceback
import os, shutil

_app = None
_ui = None

def find_thread_data_folders():
    folders = []
    local = os.environ.get('LOCALAPPDATA') or os.path.expanduser('~')
    win_bases = [
        os.path.join(local, 'Autodesk', 'webdeploy', 'Production'),
        os.path.join(local, 'Autodesk', 'webdeploy', 'production'),
    ]
    for base in win_bases:
        if os.path.isdir(base):
            for ver in sorted(os.listdir(base), reverse=True):
                for sub in ['Fusion/Server/Fusion/Configuration/ThreadData',
                            'Fusion/Server/fusion/Configuration/ThreadData']:
                    td = os.path.join(base, ver, *sub.split('/'))
                    if os.path.isdir(td):
                        folders.append(td)
    mac_base = os.path.expanduser(
        '~/Library/Application Support/Autodesk/Webdeploy/production')
    if os.path.isdir(mac_base):
        for ver in sorted(os.listdir(mac_base), reverse=True):
            td = os.path.join(mac_base, ver, 'Autodesk Fusion 360.app',
                              'Contents', 'Resources', 'Fusion', 'Server',
                              'Fusion', 'Configuration', 'ThreadData')
            if os.path.isdir(td):
                folders.append(td)
    seen, out = set(), []
    for f in folders:
        k = f.lower()
        if k not in seen:
            seen.add(k)
            out.append(f)
    return out

def run(context):
    global _app, _ui
    try:
        _app = adsk.core.Application.get()
        _ui = _app.userInterface
    except:
        return
    try:
        src = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           'LensSizeThreads.xml')
        if not os.path.exists(src):
            _ui.messageBox('LensSizeThreads.xml not found next to the add-in. '
                           'Please reinstall the add-in.',
                           'Camera Lens and Filter Threads')
            return
        folders = find_thread_data_folders()
        if not folders:
            _ui.messageBox(
                'Could not locate any Fusion 360 ThreadData folder.\\n\\n'
                'Your Fusion install may be in a non-standard location. '
                'As a fallback, copy LensSizeThreads.xml from this add-in\\'s '
                'folder into Fusion\\'s ThreadData directory manually, then '
                'restart Fusion.', 'Camera Lens and Filter Threads')
            return
        copied = 0
        for td in folders:
            dest = os.path.join(td, 'LensSizeThreads.xml')
            try:
                if (not os.path.exists(dest)) or \\
                   os.path.getmtime(src) > os.path.getmtime(dest):
                    shutil.copy2(src, dest)
                    copied += 1
            except Exception:
                pass
        if copied:
            _ui.messageBox(
                'Installed "Camera Lens and Filter Threads" into %d Fusion '
                'configuration folder(s).\\n\\nRestart Fusion 360 to see it in '
                'the Thread Type dropdown.' % copied,
                'Camera Lens and Filter Threads')
        else:
            _ui.messageBox(
                '"Camera Lens and Filter Threads" is already installed.\\n\\n'
                'Restart Fusion 360 if it does not appear in the Thread Type '
                'dropdown.', 'Camera Lens and Filter Threads')
    except:
        if _ui:
            _ui.messageBox('Error installing threads:\\n' + traceback.format_exc())

def stop(context):
    global _app, _ui
    _ui = None
    _app = None
'''

PACKAGE_CONTENTS = f'''<?xml version="1.0" encoding="utf-8"?>
<ApplicationPackage SchemaVersion="1.0" AppVersion="{VERSION}"
    Author="HairuoLiu"
    Name="Camera Lens and Filter Threads"
    Description="Adds camera lens and filter thread sizes (24-127 mm, 0.75/1.0 mm pitch) to Fusion 360's Thread Type dropdown."
    Icon="./Contents/icon.png"
    Helpfile="./Contents/help.html"
    ProductCode="{{{PRODUCT_CODE}}}"
    UpgradeCode="{{{UPGRADE_CODE}}}">
  <CompanyDetails
    Name="HairuoLiu"
    Email=""
    Url="https://github.com/HairuoLiu/fusion-lens-threads" />
  <RuntimeRequirements OS="Win64|Mac" Platform="Fusion" />
  <Components>
    <ComponentEntry
      AppName="Camera Lens and Filter Threads"
      ModuleName="./Contents/lens_thread_installer.py"
      AppDescription="Installs lens/filter thread definitions into Fusion 360." />
  </Components>
</ApplicationPackage>
'''

MANIFEST = f'''<?xml version="1.0" encoding="UTF-8"?>
<AddinManifest xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  <AutodeskProduct>Fusion360</AutodeskProduct>
  <Type>Python</Type>
  <Description>Adds camera lens and filter thread sizes to Fusion 360's Thread Type dropdown. Run once to install; restart Fusion to use.</Description>
  <Author>HairuoLiu</Author>
  <Version>{VERSION}</Version>
  <Id>CameraLensAndFilterThreads</Id>
  <Name>Camera Lens and Filter Threads</Name>
</AddinManifest>
'''

HELP_HTML = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><title>Camera Lens and Filter Threads</title></head>
<body style="font-family:system-ui,Arial,sans-serif;max-width:720px;margin:auto;padding:24px;color:#222">
<h1>Camera Lens and Filter Threads</h1>
<p>Free, open-source Fusion 360 add-in that adds standard camera lens and filter
thread sizes to the <strong>Thread Type</strong> dropdown, so you can model
step-up rings, filter adapters, lens hoods, and custom caps with real threads.</p>
<h2>What it installs</h2>
<ul>
  <li>73 sizes from 24 mm to 127 mm (covers 25, 30, 37, 39, 40.5, 43, 46, 49, 52,
      55, 58, 62, 67, 72, 77, 82, 86, 95, 105, 112, 127 mm and more).</li>
  <li>Two pitches: <strong>0.75 mm</strong> (most filter sizes) and
      <strong>1.0 mm</strong> (large filters + M39/M42 lens mounts).</li>
  <li>Both male (external) and female (internal) threads — 292 thread definitions.</li>
</ul>
<h2>How to use</h2>
<ol>
  <li>Install this add-in from the Autodesk App Store (or via Scripts &amp; Add-ins).</li>
  <li>Run it once. It copies the thread definitions into Fusion's configuration folder.</li>
  <li><strong>Restart Fusion 360.</strong></li>
  <li>In a model, create a thread (Modify &gt; Thread), open the
      <em>Thread Type</em> list, and pick <strong>Camera Lens and Filter Threads</strong>.</li>
</ol>
<h2>License</h2>
<p>MIT License. Source:
<a href="https://github.com/HairuoLiu/fusion-lens-threads">github.com/HairuoLiu/fusion-lens-threads</a></p>
</body></html>
'''


# --------------------------------------------------------------------------
# 2. Pure-python 120x120 PNG icon (a camera-lens glyph on an app-blue square)
# --------------------------------------------------------------------------
def write_png(path, w, h, rows):
    def chunk(typ, data):
        return (struct.pack('>I', len(data)) + typ + data +
                struct.pack('>I', zlib.crc32(typ + data) & 0xffffffff))
    raw = b''.join(b'\x00' + row for row in rows)
    with open(path, 'wb') as f:
        f.write(b'\x89PNG\r\n\x1a\n')
        f.write(chunk(b'IHDR', struct.pack('>IIBBBBB', w, h, 8, 6, 0, 0, 0)))
        f.write(chunk(b'IDAT', zlib.compress(raw, 9)))
        f.write(chunk(b'IEND', b''))


def make_icon(path, size=120):
    cx = cy = size / 2.0
    rows = []
    for y in range(size):
        row = bytearray()
        for x in range(size):
            dx, dy = x - cx, y - cy
            d = (dx * dx + dy * dy) ** 0.5
            if d > 56:                      # app-blue background
                r, g, b = 31, 111, 235
            elif d > 42:                    # lens barrel
                r, g, b = 25, 25, 28
            elif d > 36:                    # ring
                r, g, b = 96, 100, 108
            else:                           # glass (blue gradient by radius)
                t = max(0.0, min(1.0, (36 - d) / 36.0))
                r = int(40 + 120 * t)
                g = int(90 + 90 * t)
                b = int(180 + 60 * t)
            row += bytes((r, g, b, 255))
        rows.append(bytes(row))
    write_png(path, size, size, rows)


# --------------------------------------------------------------------------
# 3. Assemble the bundle
# --------------------------------------------------------------------------
def main():
    os.makedirs(CONTENTS, exist_ok=True)
    # core deliverable
    shutil.copy2(os.path.join(ROOT, 'LensSizeThreads.xml'),
                 os.path.join(CONTENTS, 'LensSizeThreads.xml'))
    # add-in + metadata
    with open(os.path.join(CONTENTS, 'lens_thread_installer.py'), 'w',
              encoding='utf-8', newline='\n') as f:
        f.write(ADDIN_PY)
    with open(os.path.join(BUNDLE, 'PackageContents.xml'), 'w',
              encoding='utf-8', newline='\n') as f:
        f.write(PACKAGE_CONTENTS)
    with open(os.path.join(CONTENTS, 'LensSizeThreads.Manifest'), 'w',
              encoding='utf-8', newline='\n') as f:
        f.write(MANIFEST)
    with open(os.path.join(CONTENTS, 'help.html'), 'w',
              encoding='utf-8', newline='\n') as f:
        f.write(HELP_HTML)
    make_icon(os.path.join(CONTENTS, 'icon.png'))
    # source / optional installers kept alongside for transparency
    for name in ('install_windows.ps1', 'install_mac.sh', 'generate_lens_threads.py'):
        src = os.path.join(ROOT, name)
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(CONTENTS, name))

    # syntax-check the add-in
    import py_compile
    py_compile.compile(os.path.join(CONTENTS, 'lens_thread_installer.py'),
                       doraise=True)

    # zip the bundle (skip pycache left by py_compile)
    import shutil as _shutil
    cache = os.path.join(CONTENTS, '__pycache__')
    if os.path.isdir(cache):
        _shutil.rmtree(cache)
    if os.path.exists(APP_ZIP):
        os.remove(APP_ZIP)
    with zipfile.ZipFile(APP_ZIP, 'w', zipfile.ZIP_DEFLATED) as z:
        for dp, _, fns in os.walk(BUNDLE):
            if '__pycache__' in dp.split(os.sep):
                continue
            for fn in fns:
                fp = os.path.join(dp, fn)
                arc = os.path.relpath(fp, ROOT).replace('\\', '/')
                z.write(fp, arc)
    print(f"Bundle built: {APP_ZIP}")
    print(f"Files in zip: {len(zipfile.ZipFile(APP_ZIP).namelist())}")
    for n in sorted(zipfile.ZipFile(APP_ZIP).namelist()):
        print("  ", n)


if __name__ == "__main__":
    main()
