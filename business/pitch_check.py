#!/usr/bin/env python3
"""
pitch_check.py -- character counts for the NSF SBIR Project Pitch draft against the form limits.
Run: python3 business/pitch_check.py
Limits are the ones this draft assumes [TO-VERIFY on seedfund.nsf.gov before submitting].
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
LIMITS = {"1. The Technology Innovation": 3500,
          "2. The Technical Objectives and Challenges": 3500,
          "3. The Market Opportunity": 1750,
          "4. The Company and Team": 1750}

if __name__ == "__main__":
    text = open(os.path.join(HERE, "NSF_SBIR_PROJECT_PITCH.md"), encoding="utf-8").read()
    parts = re.split(r"^## ", text, flags=re.M)
    bad = 0
    for p in parts[1:]:
        title, body = p.split("\n", 1)
        body = body.strip()
        lim = LIMITS.get(title.strip())
        if lim is None:
            continue
        n = len(body)
        ok = n <= lim
        bad += not ok
        print(f"{'ok ' if ok else 'OVER'} {title.strip():45s} {n:5d} / {lim} characters")
    sys.exit(1 if bad else 0)
