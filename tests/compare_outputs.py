#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Compare the XML produced by the three generators (Python, Mac bash, Windows
PowerShell) and assert they describe the SAME threads (same sizes, pitches,
genders, classes) with diameters matching within 0.01 mm.

Usage:
  # filter/lens family only
  python tests/compare_outputs.py <py.xml> <mac.xml> <win.xml>

  # both families (lens trio first, then the Leica/LTM trio)
  python tests/compare_outputs.py <py.xml> <mac.xml> <win.xml> \
                                  <py-ltm.xml> <mac-ltm.xml> <win-ltm.xml>
"""
import sys
import xml.etree.ElementTree as ET


def collect(path):
    root = ET.parse(path).getroot()
    rows = set()
    for ts in root.findall("ThreadSize"):
        sz = float(ts.findtext("Size"))
        for des in ts.findall("Designation"):
            pitch = float(des.findtext("Pitch"))
            for t in des.findall("Thread"):
                gender = t.findtext("Gender")
                cls = t.findtext("Class")
                major = round(float(t.findtext("MajorDia")), 2)
                pdia = round(float(t.findtext("PitchDia")), 2)
                minor = round(float(t.findtext("MinorDia")), 2)
                rows.add((sz, pitch, gender, cls, major, pdia, minor))
    return rows


def compare(label, files):
    groups = [collect(p) for p in files]
    base = groups[0]
    ok = True
    names = ("py", "mac", "win")
    for i, rows in enumerate(groups[1:], start=1):
        if rows != base:
            ok = False
            print("DIFF [{}] py vs {}:".format(label, names[i]))
            for r in sorted(base ^ rows)[:20]:
                print("  ", r)
    print("{}: {} - all three generators agree ({} threads each)".format(
        "OK" if ok else "FAIL", label, len(base)))
    return ok


def main():
    files = sys.argv[1:]
    if len(files) == 3:
        groups = [("LensSizeThreads", files)]
    elif len(files) == 6:
        groups = [("LensSizeThreads", files[:3]), ("LensMountThreads", files[3:])]
    else:
        print("usage: compare_outputs.py py.xml mac.xml win.xml "
              "[py-ltm.xml mac-ltm.xml win-ltm.xml]")
        sys.exit(2)

    ok = all(compare(label, f) for label, f in groups)

    lens_rows = collect(groups[0][1][0])
    ltm = [r for r in lens_rows if abs(r[1] - 25.4 / 26.0) < 1e-6]
    if ltm:
        print("  LTM entry (26 TPI):", sorted(ltm)[0])
    else:
        print("  WARNING: no 26 TPI (0.976923 mm) entry found in the lens family")
        ok = False

    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
