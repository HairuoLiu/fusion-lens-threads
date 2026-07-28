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
                'Could not locate any Fusion 360 ThreadData folder.\n\n'
                'Your Fusion install may be in a non-standard location. '
                'As a fallback, copy LensSizeThreads.xml from this add-in\'s '
                'folder into Fusion\'s ThreadData directory manually, then '
                'restart Fusion.', 'Camera Lens and Filter Threads')
            return
        copied = 0
        for td in folders:
            dest = os.path.join(td, 'LensSizeThreads.xml')
            try:
                if (not os.path.exists(dest)) or \
                   os.path.getmtime(src) > os.path.getmtime(dest):
                    shutil.copy2(src, dest)
                    copied += 1
            except Exception:
                pass
        if copied:
            _ui.messageBox(
                'Installed "Camera Lens and Filter Threads" into %d Fusion '
                'configuration folder(s).\n\nRestart Fusion 360 to see it in '
                'the Thread Type dropdown.' % copied,
                'Camera Lens and Filter Threads')
        else:
            _ui.messageBox(
                '"Camera Lens and Filter Threads" is already installed.\n\n'
                'Restart Fusion 360 if it does not appear in the Thread Type '
                'dropdown.', 'Camera Lens and Filter Threads')
    except:
        if _ui:
            _ui.messageBox('Error installing threads:\n' + traceback.format_exc())

def stop(context):
    global _app, _ui
    _ui = None
    _app = None
