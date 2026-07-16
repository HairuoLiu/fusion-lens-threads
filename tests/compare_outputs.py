#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Compare the XML produced by the three generators (Python, Mac bash, Windows
PowerShell) and assert they describe the SAME threads (same sizes, pitches,
genders, classes) with diameters matching within 0.01 mm.

Usage:
  python tests/compare_outputs.py <py.xml> <mac.xml> <win.xml>
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


def main():
    if len(sys.argv) != 4:
        print("usage: compare_outputs.py py.xml mac.xml win.xml")
        sys.exit(2)
    py, mac, win = (collect(p) for p in sys.argv[1:])

    ok = True
    if py != mac:
        ok = False
        print("DIFF py vs mac:")
        for r in sorted(py ^ mac)[:20]:
            print("  ", r)
    if py != win:
        ok = False
        print("DIFF py vs win:")
        for r in sorted(py ^ win)[:20]:
            print("  ", r)

    if ok:
        print("OK: all three generators produce identical threads ({} threads each)".format(len(py)))
        print("  sample: M42x1 external  ->",
              [r for r in py if r[0] == 42 and r[1] == 1.0 and r[2] == "external"][0])
        print("  sample: M42x1 internal  ->",
              [r for r in py if r[0] == 42 and r[1] == 1.0 and r[2] == "internal"][0])
        sys.exit(0)
    sys.exit(1)


if __name__ == "__main__":
    main()
