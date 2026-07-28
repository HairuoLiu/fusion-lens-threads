"""Build a clean distribution ZIP for a GitHub release.

Usage: python build_release.py [output_zip]
Excludes .git, .workbuddy, logs, and the output zip itself.
"""
import os
import sys
import zipfile

ROOT = "."
OUT = sys.argv[1] if len(sys.argv) > 1 else "fusion-lens-threads-v1.1.0.zip"
SKIP_DIRS = {".git", ".workbuddy", "__pycache__", "node_modules"}


def keep(path: str) -> bool:
    parts = path.split(os.sep)
    if any(p in SKIP_DIRS for p in parts):
        return False
    base = os.path.basename(path)
    if base == OUT:
        return False
    if base.endswith(".log"):
        return False
    return True


def main() -> None:
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
        for dp, _, fns in os.walk(ROOT):
            if not keep(dp):
                continue
            for fn in fns:
                fp = os.path.join(dp, fn)
                if not keep(fp):
                    continue
                arc = fp.replace(".\\", "/").replace("\\", "/")
                z.write(fp, arc)
    print(f"Wrote {OUT}: {os.path.getsize(OUT)} bytes, "
          f"{len(zipfile.ZipFile(OUT).namelist())} files")


if __name__ == "__main__":
    main()
