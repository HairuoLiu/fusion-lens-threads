#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validate a generated LensSizeThreads.xml against the project spec.

Checks:
  * well-formed XML, root <ThreadType>
  * family Name == 镜头尺寸螺纹规格, Unit == mm, Angle == 60
  * every diameter in SIZES is present as a <ThreadSize>
  * every size has BOTH pitch 0.75 and 1.0 designations (Mxx x pitch)
  * every designation has both external (6g) and internal (6H) threads
  * MajorDia > PitchDia > MinorDia > 0 for every thread

Usage:
  python tests/test_threads.py [path/to/LensSizeThreads.xml]
"""

import sys
import os
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import generate_lens_threads as gen  # noqa: E402


def design_for(size, pitch):
    return "M{}x{}".format(gen.fmt(size), gen.fmt(pitch))


def main():
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = os.path.join(os.path.dirname(HERE), "LensSizeThreads.xml")

    if not os.path.exists(path):
        print("FAIL: file not found: {}".format(path))
        sys.exit(1)

    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as e:
        print("FAIL: XML is not well-formed: {}".format(e))
        sys.exit(1)

    errors = []

    if root.tag != "ThreadType":
        errors.append("root tag is <{}>, expected <ThreadType>".format(root.tag))

    if (root.findtext("Name") or "") != gen.FAMILY_NAME:
        errors.append("Name is {!r}, expected {!r}".format(
            root.findtext("Name"), gen.FAMILY_NAME))
    if (root.findtext("CustomName") or "") != gen.FAMILY_NAME:
        errors.append("CustomName mismatch")
    if (root.findtext("Unit") or "") != "mm":
        errors.append("Unit is {!r}, expected 'mm'".format(root.findtext("Unit")))
    try:
        if abs(float(root.findtext("Angle")) - 60) > 1e-6:
            errors.append("Angle is {}, expected 60".format(root.findtext("Angle")))
    except (TypeError, ValueError) as e:
        errors.append("Angle unparseable: {}".format(e))

    # Map size -> {designation: (pitch, [genders])}
    sizes = {}
    for ts in root.findall("ThreadSize"):
        try:
            sz = float(ts.findtext("Size"))
        except (TypeError, ValueError):
            errors.append("ThreadSize with missing/invalid <Size>")
            continue
        for des in ts.findall("Designation"):
            td = des.findtext("ThreadDesignation") or ""
            pitch = des.findtext("Pitch")
            genders = [t.findtext("Gender") for t in des.findall("Thread")]
            sizes.setdefault(sz, {})[td] = (pitch, genders)

    # every configured size present
    for s in gen.SIZES:
        if s not in sizes:
            errors.append("size {} missing entirely".format(s))

    # every size has both required pitches
    for s in gen.SIZES:
        for p in gen.PITCHES:
            d = design_for(s, p)
            if d not in sizes.get(s, {}):
                errors.append("designation {} missing for size {}".format(d, s))

    # every designation has external + internal
    for s, desmap in sizes.items():
        for design, (pitch, genders) in desmap.items():
            if "external" not in genders or "internal" not in genders:
                errors.append("{}: missing gender(s) {}".format(design, genders))

    # diameter sanity for every thread
    count = 0
    for ts in root.findall("ThreadSize"):
        for des in ts.findall("Designation"):
            for t in des.findall("Thread"):
                count += 1
                try:
                    major = float(t.findtext("MajorDia"))
                    pdia = float(t.findtext("PitchDia"))
                    minor = float(t.findtext("MinorDia"))
                except (TypeError, ValueError):
                    errors.append("{} / {}: non-numeric diameter".format(
                        des.findtext("ThreadDesignation"), t.findtext("Gender")))
                    continue
                if not (major > pdia > minor > 0):
                    errors.append("{} / {}: bad diameters major={} pitch={} minor={}".format(
                        des.findtext("ThreadDesignation"),
                        t.findtext("Gender"), major, pdia, minor))

    if errors:
        print("VALIDATION FAILED ({} issue(s)):".format(len(errors)))
        for e in errors[:60]:
            print("  - " + e)
        sys.exit(1)

    print("OK: {}".format(path))
    print("  family name (shows in Fusion 360): {}".format(gen.FAMILY_NAME))
    print("  sizes covered : {} ({} mm .. {} mm)".format(
        len(gen.SIZES), min(gen.SIZES), max(gen.SIZES)))
    print("  pitches        : {}".format(gen.PITCHES))
    print("  total threads  : {}".format(count))


if __name__ == "__main__":
    main()
