import adsk.core, adsk.fusion, traceback
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
        here = os.path.dirname(os.path.abspath(__file__))
        # Both families are shipped by the add-in:
        #   LensSizeThreads.xml  - filter/lens threads (0.75 / 1.0 mm) + the
        #                          Leica Thread Mount pitch L39x1/26-LTM
        #   LensMountThreads.xml - L39 / LTM with the Whitworth 55 deg form
        payloads = ['LensSizeThreads.xml', 'LensMountThreads.xml']
        sources = [(name, os.path.join(here, name)) for name in payloads]
        missing = [n for n, s in sources if not os.path.exists(s)]
        if missing:
            _ui.messageBox('%s not found next to the add-in. '
                           'Please reinstall the add-in.' % ', '.join(missing),
                           'Camera Lens and Filter Threads')
            return
        folders = find_thread_data_folders()
        if not folders:
            _ui.messageBox(
                'Could not locate any Fusion 360 ThreadData folder.\n\n'
                'Your Fusion install may be in a non-standard location. '
                'As a fallback, copy the thread XML files from this add-in\'s '
                'folder into Fusion\'s ThreadData directory manually, then '
                'restart Fusion.', 'Camera Lens and Filter Threads')
            return
        copied = 0
        for td in folders:
            for name, src in sources:
                dest = os.path.join(td, name)
                try:
                    if (not os.path.exists(dest)) or \
                       os.path.getmtime(src) > os.path.getmtime(dest):
                        shutil.copy2(src, dest)
                        copied += 1
                except Exception:
                    pass
        if copied:
            _ui.messageBox(
                'Installed %d thread file(s):\n'
                '  - Camera Lens and Filter Threads (incl. L39x1/26-LTM)\n'
                '  - Leica Thread Mount (L39/LTM, Whitworth 55 deg)\n\n'
                'into %d Fusion configuration folder(s).\n\n'
                'Restart Fusion 360 to see them in the Thread Type dropdown.'
                % (copied, len(folders)),
                'Camera Lens and Filter Threads')
        else:
            _ui.messageBox(
                'Both thread families are already installed.\n\n'
                'Restart Fusion 360 if they do not appear in the Thread Type '
                'dropdown.', 'Camera Lens and Filter Threads')
    except:
        if _ui:
            _ui.messageBox('Error installing threads:\n' + traceback.format_exc())

def stop(context):
    global _app, _ui
    _ui = None
    _app = None
