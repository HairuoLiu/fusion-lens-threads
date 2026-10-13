#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validate the generated Fusion 360 thread XML files against the project spec.

Files checked (defaults, in the repository root):
  LensSizeThreads.xml   - "Camera Lens and Filter Threads" (60 deg)
  LensMountThreads.xml  - "Leica Thread Mount (L39/LTM)"   (55 deg Whitworth)

Checks on LensSizeThreads.xml:
  * well-formed XML, root <ThreadType>
  * family Name/CustomName, Unit == mm, Angle == 60
  * every diameter in SIZES is present as a <ThreadSize>
  * every size has BOTH pitch 0.75 and 1.0 designations
  * every SPECIAL_DESIGNATIONS entry is present with its exact pitch
    (e.g. M39x1/26-LTM at 0.976923 mm = 26 TPI)
  * every designation has both external (6g) and internal (6H) threads
  * MajorDia > PitchDia > MinorDia > 0 for every thread

Checks on LensMountThreads.xml:
  * well-formed XML, Name == LTM_FAMILY_NAME, Angle == 55
  * every LTM_SIZES entry present with the correct 26 TPI pitch
  * Whitworth pitch/minor diameters match d - 0.640327P / d - 1.280655P
  * both genders present, sane diameters

Usage:
  python tests/test_threads.py [path/to/LensSizeThreads.xml] [path/to/LensMountThreads.xml]
"""

import sys
import os
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
import generate_lens_threads as gen  # noqa: E402


def design_for(size, pitch):
    return "M{}x{}".format(gen.fmt(size), gen.fmt_pitch(pitch))


def index_file(root):
    """size -> designation -> (pitch, [genders])"""
    sizes = {}
    for ts in root.findall("ThreadSize"):
        try:
            sz = float(ts.findtext("Size"))
        except (TypeError, ValueError):
            continue
        for des in ts.findall("Designation"):
            td = des.findtext("ThreadDesignation") or ""
            pitch = des.findtext("Pitch")
            genders = [t.findtext("Gender") for t in des.findall("Thread")]
            sizes.setdefault(sz, {})[td] = (pitch, genders)
    return sizes


def check_sane_diameters(root, errors, count):
    for ts in root.findall("ThreadSize"):
        for des in ts.findall("Designation"):
            for t in des.findall("Thread"):
                count[0] += 1
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
    return count


def check_lens_file(path, errors):
    root = ET.parse(path).getroot()
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

    sizes = index_file(root)

    for s in gen.SIZES:
        if s not in sizes:
            errors.append("size {} missing entirely".format(s))
    for s in gen.SIZES:
        for p in gen.PITCHES:
            d = design_for(s, p)
            if d not in sizes.get(s, {}):
                errors.append("designation {} missing for size {}".format(d, s))

    # special (non-metric) designations, e.g. L39 / LTM 26 TPI
    for s, label, p in gen.SPECIAL_DESIGNATIONS:
        entry = sizes.get(float(s), {}).get(label)
        if entry is None:
            errors.append("special designation {} missing for size {}".format(label, s))
            continue
        try:
            if abs(float(entry[0]) - p) > 1e-6:
                errors.append("{} pitch is {}, expected {}".format(label, entry[0], p))
        except (TypeError, ValueError):
            errors.append("{} pitch unparseable".format(label))

    for sz, desmap in sizes.items():
        for design, (pitch, genders) in desmap.items():
            if "external" not in genders or "internal" not in genders:
                errors.append("{}: missing gender(s) {}".format(design, genders))

    count = [0]
    check_sane_diameters(root, errors, count)
    return count[0]


def check_ltm_file(path, errors):
    root = ET.parse(path).getroot()
    if root.tag != "ThreadType":
        errors.append("[LTM] root tag is <{}>, expected <ThreadType>".format(root.tag))
    if (root.findtext("Name") or "") != gen.LTM_FAMILY_NAME:
        errors.append("[LTM] Name is {!r}, expected {!r}".format(
            root.findtext("Name"), gen.LTM_FAMILY_NAME))
    try:
        if abs(float(root.findtext("Angle")) - 55) > 1e-6:
            errors.append("[LTM] Angle is {}, expected 55 (Whitworth)".format(
                root.findtext("Angle")))
    except (TypeError, ValueError) as e:
        errors.append("[LTM] Angle unparseable: {}".format(e))

    sizes = index_file(root)
    for s, label, p in gen.LTM_SIZES:
        entry = sizes.get(float(s), {}).get(label)
        if entry is None:
            errors.append("[LTM] designation {} missing for size {}".format(label, s))
            continue
        try:
            if abs(float(entry[0]) - p) > 1e-6:
                errors.append("[LTM] {} pitch is {}, expected {}".format(
                    label, entry[0], p))
        except (TypeError, ValueError):
            errors.append("[LTM] {} pitch unparseable".format(label))
        if "external" not in entry[1] or "internal" not in entry[1]:
            errors.append("[LTM] {}: missing gender(s) {}".format(label, entry[1]))

    # Whitworth geometry: d2 = d - 0.640327P, d1 = d - 1.280655P (+/- allowance)
    for ts in root.findall("ThreadSize"):
        sz = float(ts.findtext("Size"))
        for des in ts.findall("Designation"):
            p = float(des.findtext("Pitch"))
            depth = gen.WHITWORTH_DEPTH * p
            for t in des.findall("Thread"):
                sign = -1.0 if t.findtext("Gender") == "external" else 1.0
                exp_pd = sz - depth + sign * gen.ALLOWANCE
                exp_md = sz - 2.0 * depth + sign * gen.ALLOWANCE
                got_pd = float(t.findtext("PitchDia"))
                got_md = float(t.findtext("MinorDia"))
                if abs(got_pd - exp_pd) > 1e-3 or abs(got_md - exp_md) > 1e-3:
                    errors.append(
                        "[LTM] {} / {}: pitch dia {} (expected {:.4f}), "
                        "minor dia {} (expected {:.4f})".format(
                            des.findtext("ThreadDesignation"), t.findtext("Gender"),
                            got_pd, exp_pd, got_md, exp_md))

    count = [0]
    check_sane_diameters(root, errors, count)
    return count[0]


def main():
    lens_path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "LensSizeThreads.xml")
    ltm_path = sys.argv[2] if len(sys.argv) > 2 else os.path.join(ROOT, "LensMountThreads.xml")

    for p in (lens_path, ltm_path):
        if not os.path.exists(p):
            print("FAIL: file not found: {}".format(p))
            sys.exit(1)

    errors = []
    try:
        n_lens = check_lens_file(lens_path, errors)
    except ET.ParseError as e:
        print("FAIL: {} is not well-formed: {}".format(lens_path, e))
        sys.exit(1)
    try:
        n_ltm = check_ltm_file(ltm_path, errors)
    except ET.ParseError as e:
        print("FAIL: {} is not well-formed: {}".format(ltm_path, e))
        sys.exit(1)

    if errors:
        print("VALIDATION FAILED ({} issue(s)):".format(len(errors)))
        for e in errors[:60]:
            print("  - " + e)
        sys.exit(1)

    print("OK: {}".format(lens_path))
    print("  family name (shows in Fusion 360): {}".format(gen.FAMILY_NAME))
    print("  sizes covered : {} ({} mm .. {} mm)".format(
        len(gen.SIZES), min(gen.SIZES), max(gen.SIZES)))
    print("  pitches       : {}".format(gen.PITCHES))
    print("  special       : {}".format(
        ", ".join("{} @ {} mm".format(l, round(p, 6)) for _, l, p in gen.SPECIAL_DESIGNATIONS)))
    print("  total threads : {}".format(n_lens))
    print("OK: {}".format(ltm_path))
    print("  family name   : {} (Whitworth 55 deg)".format(gen.LTM_FAMILY_NAME))
    print("  designations  : {}".format(
        ", ".join("{} @ {} mm".format(l, round(p, 6)) for _, l, p in gen.LTM_SIZES)))
    print("  total threads : {}".format(n_ltm))


if __name__ == "__main__":
    main()
