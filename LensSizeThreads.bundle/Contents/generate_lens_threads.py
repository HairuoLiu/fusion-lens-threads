#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate LensSizeThreads.xml for Autodesk Fusion 360.

Creates a custom thread family named "Camera Lens and Filter Threads" that
appears in Fusion 360's Thread command under "Thread Type".

It covers every common camera-lens / filter thread diameter (24 mm .. 127 mm)
with BOTH a 0.75 mm pitch and a 1.0 mm pitch, so any lens (e.g. the
M42x1 mount or a 42 mm filter ring) can be modeled and screwed in.

Geometry follows the basic ISO metric 60-degree profile:
    H      = (sqrt(3)/2) * pitch
    d2     = d - 0.75 * H      (pitch diameter)
    d3/d1  = d - 1.25 * H      (minor diameter)
External threads are shrunk by ALLOWANCE and internal threads grown by the same
amount, guaranteeing that an external (lens barrel) thread fits into an
internal (filter ring) thread of the same nominal size.

This script is also used by the test harness (tests/test_threads.py).
"""

import sys
import os
import math

# ---------------------------------------------------------------------------
# Configuration (single source of truth for the Python generator)
# ---------------------------------------------------------------------------

# Family name shown in Fusion 360's "Thread Type" dropdown.
FAMILY_NAME = "Camera Lens and Filter Threads"

UNIT = "mm"
ANGLE = 60.0
SORT_ORDER = 100

# Clearance (mm) applied so an external thread fits into an internal one.
ALLOWANCE = 0.10

# Comprehensive photographic lens / filter thread diameters (mm).
# Covers the standard filter series from 24 mm up to 127 mm, including the
# sizes the user explicitly asked for (39, 40, 42, 43, ...).
SIZES = [
    24, 25, 25.5, 27, 28, 30, 30.5, 34, 35.5, 36, 36.5, 37, 37.5,
    38.5, 39, 40, 40.5, 41, 42, 43, 43.5, 44, 46, 46.5, 48, 49, 50,
    50.5, 52, 54, 55, 56, 58, 60, 62, 64, 67, 70, 72, 74, 75, 76, 77,
    78, 80, 82, 84, 85, 86, 87, 90, 92, 94, 95, 96, 98, 100, 102, 104,
    105, 107, 108, 110, 112, 114, 116, 118, 120, 122, 124, 125, 126, 127,
]

# Pitches required by the user: 0.75 mm and 1.0 mm.
PITCHES = [0.75, 1.0]


def fmt(x):
    """Format a number the way Fusion 360 expects: integers without a
    trailing '.0', otherwise up to 4 decimal places with trailing zeros
    stripped (e.g. 0.75, 40.5, 1, 39)."""
    x = float(x)
    if abs(x - round(x)) < 1e-9:
        return str(int(round(x)))
    return ("{:.4f}".format(x)).rstrip("0").rstrip(".")


def compute(nominal, pitch, gender):
    """Return dict with major/pitch/minor diameters for one thread.

    gender is 'external' (shrunk) or 'internal' (grown) by ALLOWANCE.
    """
    H = math.sqrt(3.0) / 2.0 * pitch
    pitch_dia_basic = nominal - 0.75 * H
    minor_dia_basic = nominal - 1.25 * H
    sign = -1.0 if gender == "external" else 1.0
    return {
        "major": nominal + sign * ALLOWANCE,
        "pitch": pitch_dia_basic + sign * ALLOWANCE,
        "minor": minor_dia_basic + sign * ALLOWANCE,
    }


def build_xml():
    """Build the complete Fusion 360 thread XML as a string."""
    L = []
    L.append('<?xml version="1.0" encoding="UTF-8"?>')
    L.append("<ThreadType>")
    L.append("  <Name>{}</Name>".format(FAMILY_NAME))
    L.append("  <CustomName>{}</CustomName>".format(FAMILY_NAME))
    L.append("  <Unit>{}</Unit>".format(UNIT))
    L.append("  <Angle>{}</Angle>".format(fmt(ANGLE)))
    L.append("  <SortOrder>{}</SortOrder>".format(SORT_ORDER))

    for size in SIZES:
        L.append("  <ThreadSize>")
        L.append("    <Size>{}</Size>".format(fmt(size)))
        for pitch in PITCHES:
            design = "M{}x{}".format(fmt(size), fmt(pitch))
            L.append("    <Designation>")
            L.append("      <ThreadDesignation>{}</ThreadDesignation>".format(design))
            L.append("      <CTD>{}</CTD>".format(design))
            L.append("      <Pitch>{}</Pitch>".format(fmt(pitch)))
            for gender, cls in (("external", "6g"), ("internal", "6H")):
                d = compute(size, pitch, gender)
                L.append("      <Thread>")
                L.append("        <Gender>{}</Gender>".format(gender))
                L.append("        <Class>{}</Class>".format(cls))
                L.append("        <MajorDia>{}</MajorDia>".format(fmt(d["major"])))
                L.append("        <PitchDia>{}</PitchDia>".format(fmt(d["pitch"])))
                L.append("        <MinorDia>{}</MinorDia>".format(fmt(d["minor"])))
                L.append("      </Thread>")
            L.append("    </Designation>")
        L.append("  </ThreadSize>")
    L.append("</ThreadType>")
    return "\n".join(L) + "\n"


def main():
    out = "LensSizeThreads.xml"
    if len(sys.argv) > 1:
        out = sys.argv[1]
    xml = build_xml()
    with open(out, "w", encoding="utf-8") as f:
        f.write(xml)
    print("Wrote {} ({} sizes x {} pitches = {} threads)".format(
        out, len(SIZES), len(PITCHES), len(SIZES) * len(PITCHES) * 2))


if __name__ == "__main__":
    main()
