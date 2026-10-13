#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate the Fusion 360 custom-thread XML files for camera work.

Two files are produced:

  1. LensSizeThreads.xml  ->  family "Camera Lens and Filter Threads" (60 deg)
     Every common lens / filter diameter (24 .. 127 mm) in 0.75 mm and 1.0 mm
     pitch, PLUS the special Leica Thread Mount pitch on 39 mm:
     M39 x 1/26" (26 TPI) = 25.4/26 = 0.976923 mm  ->  "M39x1/26-LTM".

  2. LensMountThreads.xml ->  family "Leica Thread Mount (L39/LTM)" (55 deg)
     The historically correct Whitworth-form L39 mount: 39 mm x 26 TPI with a
     55 deg flank angle. (Flange focal distance of 28.8 mm is a body/lens
     dimension, not a thread dimension - set it in your model.)

Geometry
    ISO metric 60 deg (file 1):
        H  = (sqrt(3)/2) * pitch
        d2 = d - 0.75 * H          (pitch diameter)
        d1 = d - 1.25 * H          (minor diameter)
    Whitworth 55 deg (file 2):
        d2 = d - 0.640327 * pitch
        d1 = d - 1.280655 * pitch  (2 x 0.640327 P)

External threads are shrunk by ALLOWANCE and internal threads grown by the
same amount, guaranteeing an external thread fits an internal one of the
same nominal size.

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
SIZES = [
    24, 25, 25.5, 27, 28, 30, 30.5, 34, 35.5, 36, 36.5, 37, 37.5,
    38.5, 39, 40, 40.5, 41, 42, 43, 43.5, 44, 46, 46.5, 48, 49, 50,
    50.5, 52, 54, 55, 56, 58, 60, 62, 64, 67, 70, 72, 74, 75, 76, 77,
    78, 80, 82, 84, 85, 86, 87, 90, 92, 94, 95, 96, 98, 100, 102, 104,
    105, 107, 108, 110, 112, 114, 116, 118, 120, 122, 124, 125, 126, 127,
]

# Standard photographic pitches.
PITCHES = [0.75, 1.0]

# ---------------------------------------------------------------------------
# Special (non-metric) mount threads
# ---------------------------------------------------------------------------
# Leica Thread Mount (L39 / LTM / LSM): 39 mm diameter, 26 threads per inch.
# Pitch = 25.4 mm / 26 = 0.976923 mm.  NOT 1.0 mm and NOT 0.75 mm.
LTM_PITCH = 25.4 / 26.0

# (nominal size, designation label, pitch) - appended to the standard
# designations of that size.
SPECIAL_DESIGNATIONS = [
    (39, "M39x1/26-LTM", LTM_PITCH),
]

# Second family: the same mount with the correct Whitworth 55 deg flank angle.
LTM_FAMILY_NAME = "Leica Thread Mount (L39/LTM)"
LTM_ANGLE = 55.0
LTM_SORT_ORDER = 101
LTM_SIZES = [
    (39, "M39x1/26", LTM_PITCH),  # L39 / LTM, 26 TPI, flange focus 28.8 mm
]

# Whitworth form constants (radial depth of one flank = 0.640327 P).
WHITWORTH_DEPTH = 0.640327


def fmt(x):
    """Format a number the way Fusion 360 expects: integers without a
    trailing '.0', otherwise up to 4 decimal places with trailing zeros
    stripped (e.g. 0.75, 40.5, 1, 39)."""
    x = float(x)
    if abs(x - round(x)) < 1e-9:
        return str(int(round(x)))
    return ("{:.4f}".format(x)).rstrip("0").rstrip(".")


def fmt_pitch(x):
    """Format a pitch: 6 decimals (trailing zeros stripped).

    Needed because imperial-derived pitches such as 26 TPI (0.976923 mm) lose
    meaningful precision at 4 decimals.
    """
    x = float(x)
    if abs(x - round(x)) < 1e-9:
        return str(int(round(x)))
    return ("{:.6f}".format(x)).rstrip("0").rstrip(".")


def compute(nominal, pitch, gender):
    """Return dict with major/pitch/minor diameters for one 60 deg thread.

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


def compute_whitworth(nominal, pitch, gender):
    """Return dict with major/pitch/minor diameters for a 55 deg Whitworth
    thread (e.g. the Leica Thread Mount)."""
    depth = WHITWORTH_DEPTH * pitch
    pitch_dia_basic = nominal - depth
    minor_dia_basic = nominal - 2.0 * depth
    sign = -1.0 if gender == "external" else 1.0
    return {
        "major": nominal + sign * ALLOWANCE,
        "pitch": pitch_dia_basic + sign * ALLOWANCE,
        "minor": minor_dia_basic + sign * ALLOWANCE,
    }


def designations_for(size):
    """All (label, pitch) designations to emit for a given nominal size."""
    out = [("M{}x{}".format(fmt(size), fmt_pitch(p)), p) for p in PITCHES]
    out += [(label, p) for (s, label, p) in SPECIAL_DESIGNATIONS if s == size]
    return out


def _emit_designation(L, label, pitch, dims_fn):
    L.append("    <Designation>")
    L.append("      <ThreadDesignation>{}</ThreadDesignation>".format(label))
    L.append("      <CTD>{}</CTD>".format(label))
    L.append("      <Pitch>{}</Pitch>".format(fmt_pitch(pitch)))
    for gender, cls in (("external", "6g"), ("internal", "6H")):
        d = dims_fn(pitch, gender)
        L.append("      <Thread>")
        L.append("        <Gender>{}</Gender>".format(gender))
        L.append("        <Class>{}</Class>".format(cls))
        L.append("        <MajorDia>{}</MajorDia>".format(fmt(d["major"])))
        L.append("        <PitchDia>{}</PitchDia>".format(fmt(d["pitch"])))
        L.append("        <MinorDia>{}</MinorDia>".format(fmt(d["minor"])))
        L.append("      </Thread>")
    L.append("    </Designation>")


def build_xml():
    """Build the complete Fusion 360 filter/lens thread XML as a string."""
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
        for label, pitch in designations_for(size):
            _emit_designation(
                L, label, pitch,
                lambda p, g: compute(size, p, g))
        L.append("  </ThreadSize>")
    L.append("</ThreadType>")
    return "\n".join(L) + "\n"


def build_ltm_xml():
    """Build the Whitworth-form Leica Thread Mount family XML as a string."""
    L = []
    L.append('<?xml version="1.0" encoding="UTF-8"?>')
    L.append("<ThreadType>")
    L.append("  <Name>{}</Name>".format(LTM_FAMILY_NAME))
    L.append("  <CustomName>{}</CustomName>".format(LTM_FAMILY_NAME))
    L.append("  <Unit>{}</Unit>".format(UNIT))
    L.append("  <Angle>{}</Angle>".format(fmt(LTM_ANGLE)))
    L.append("  <SortOrder>{}</SortOrder>".format(LTM_SORT_ORDER))

    for size, label, pitch in LTM_SIZES:
        L.append("  <ThreadSize>")
        L.append("    <Size>{}</Size>".format(fmt(size)))
        _emit_designation(
            L, label, pitch,
            lambda p, g: compute_whitworth(size, p, g))
        L.append("  </ThreadSize>")
    L.append("</ThreadType>")
    return "\n".join(L) + "\n"


def main():
    outdir = "."
    if len(sys.argv) > 1:
        outdir = sys.argv[1]

    lens_out = os.path.join(outdir, "LensSizeThreads.xml")
    ltm_out = os.path.join(outdir, "LensMountThreads.xml")

    with open(lens_out, "w", encoding="utf-8") as f:
        f.write(build_xml())
    with open(ltm_out, "w", encoding="utf-8") as f:
        f.write(build_ltm_xml())

    n_std = len(SIZES) * len(PITCHES)
    n_special = len(SPECIAL_DESIGNATIONS)
    print("Wrote {} ({} sizes x {} pitches + {} special = {} designations, {} threads)".format(
        lens_out, len(SIZES), len(PITCHES), n_special, n_std + n_special,
        (n_std + n_special) * 2))
    print("Wrote {} ({} Whitworth mount designation(s), {} threads)".format(
        ltm_out, len(LTM_SIZES), len(LTM_SIZES) * 2))


if __name__ == "__main__":
    main()
