#!/usr/bin/env python3
"""
check_numbers.py -- the honesty layer's test. Run: python3 check_numbers.py
1. runs every script and fails if any of them errors
2. recomputes the headline numbers and fails if MISSION.md doesn't state them exactly
When a script's inputs change, this tells you which lines of MISSION.md are now stale.
Exit code 0 = everything consistent.
"""
import os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "printer"))

SCRIPTS = ["system_sizing.py", "shipping_manifest.py", "costs_estimate.py", "tiltup_check.py",
           "build_timeline.py", "site_profile.py", "lime_heat.py", "nodig_check.py",
           "printer/print_check.py", "earth-panel/energy_estimate.py",
           "rock_options.py", "brick_panel_check.py",
           "thermal_check.py", "form_check.py",
           "dome_check.py", "dome_thrust.py", "house_designer.py",
           "cladding_check.py", "drainage_check.py", "business_model.py", "dome_ribbed.py", "production_line.py",
           "business/pitch_check.py"]


def run_all():
    bad = []
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    for s in SCRIPTS:
        r = subprocess.run([sys.executable, os.path.join(HERE, s)], cwd=HERE, env=env,
                           capture_output=True, text=True, encoding="utf-8")
        print(f"  {'ok ' if r.returncode == 0 else 'ERR'} {s}")
        if r.returncode:
            bad.append((s, r.stderr.strip().splitlines()[-1:] or ["?"]))
    return bad


def dash(a, b):
    return f"{a}–{b}"


def usd(x):
    return f"${x:,.0f}"


def k(x, nd=0):
    return f"{x/1000:.{nd}f}k"


def claims():
    """(what, exact text that must appear in MISSION.md)"""
    import costs_estimate as c
    import tiltup_check as t
    import lime_heat as lh
    import print_check as pc
    import shipping_manifest as sm
    from common import PERSON_DAYS, MOR_SAFETY, F_C, lift_moments, flexural_capacity, \
        PANEL_H, PANEL_W, PANEL_T, RHO_LIFT, G, IMPACT, BAR4_AREA

    out = []
    for dims, label in [((8, 4, 6), "8×4 ft × 6 in"), ((8, 4, 8), "8×4 ft × 8 in"),
                        ((8, 16, 6), "8×16 ft × 6 in")]:
        r = t.lift_stresses(dims)
        out.append((f"lift row {label}",
                    f"| {label} (~{r['mass']:,.0f} kg) | {r['top']:.2f} MPa | **{r['opt']:.2f} MPa** |"))
    r = t.lift_stresses()
    out.append(("required MOR", f"≥ {r['opt']*MOR_SAFETY:.2f} MPa"))
    s = t.steel()
    m = [cap[0] / s["Md"] for cap in s["caps"]]
    out.append(("steel margin", f"{m[0]:.1f}–{m[1]:.1f}×"))
    out.append(("bond demand", f"~{s['bond']:.2f} MPa"))
    b = t.breakaway()
    out.append(("breakaway", f"{b[0]:.2f}–{b[1]:.2f} MPa"))
    ss = t.steel(f=0.90, depth="surface")
    ms = [cap[0] / ss["Md"] for cap in ss["caps"]]
    out.append(("surface-grid margin", f"{ms[0]:.1f}–{ms[1]:.1f}×"))
    out.append(("surface-grid bond", f"~{ss['bond']:.2f} MPa"))
    st, dyn = t.hoist()
    out.append(("hoist load", f"~{dyn:,.0f} kg"))
    out.append(("setting load", f"~{t.setting()[1]:,.0f} kg"))

    # no-dig mid-depth bars
    L, bw, h = PANEL_H, PANEL_W, PANEL_T
    w = RHO_LIFT * L * bw * h * G / L
    Md = max(lift_moments(w, L, 0.60 * L)) * IMPACT
    caps = [flexural_capacity(4 * BAR4_AREA, h / 2, bw, fc * 1e6)[0] / Md for fc in F_C]
    out.append(("no-dig mid-depth bar margin", f"{caps[0]:.1f}–{caps[1]:.1f}×"))

    # energy and costs
    out.append(("kiln energy per house", f"~{round(c.fire_kwh[0], -2):,.0f}–{round(c.fire_kwh[1], -2):,.0f} kWh"))
    out.append(("kiln days per house", f"{c.days_per_house[0]:.0f}–{c.days_per_house[1]:.0f} sunny days"))
    ph = c.total(c.PER_HOUSE)
    out.append(("per house ex roof", dash(usd(ph[0]), f"{ph[1]:,.0f}")))
    for name, d in [("rig", c.RIG), ("power", c.POWER), ("field", c.FIELD)]:
        lo, hi = c.total(d)
        out.append((name, dash(usd(lo), f"{hi:,.0f}")))
    scen = [("steel regional", {}),
            ("steel ship-all", dict(logistics="ship everything (3 containers)")),
            ("vault regional", dict(roof="earth vault + membrane (arid sites)")),
            ("next village", dict(include_rig=False))]
    for label, kw in scen:
        lo, hi = c.village(**kw)
        out.append((f"village {label}", f"${k(lo)}–{k(hi)} | ${k(lo/10, 1)}–{k(hi/10, 1)}"))
    pw = c.total(c.POWER)
    lo, hi = c.village()
    out.append(("power share", f"{pw[1]/hi*100:.0f}–{pw[0]/lo*100:.0f}%"))
    pa = c.total(c.PHASE_A)
    out.append(("Phase A total", f"${k(pa[0], 1)}–{k(pa[1], 1)}"))
    out.append(("person-days", f"{PERSON_DAYS[0]}–{PERSON_DAYS[1]} person-days"))
    out.append(("cement bags", f"~{c.cement_bags[0]:.0f}–{c.cement_bags[1]:.0f} bags"))

    # lime
    heat = [c_ * lh.Q_PER_KG / lh.KWH for c_ in (lh.PANEL_KG * f for f in lh.LIME_FRAC)]
    out.append(("lime heat per panel", f"~{heat[0]:.0f}–{heat[1]:.0f} kWh"))
    bound = [pc.lime_water(f) for f in pc.CAO_FRAC]
    out.append(("lime binds water", f"{100*bound[0][1]/bound[0][0]:.0f}–{100*bound[1][1]/bound[1][0]:.0f}%"))

    # shipping
    def tot(parts):
        return sum(p[0] for p in parts) / 1000, sum(p[1] for p in parts)
    ev = tot([sm.tot(sm.RIG), sm.tot(sm.POWER), sm.tot(sm.PER_HOUSE, 10)])
    rg = tot([sm.tot(sm.RIG)])
    out.append(("ship everything", f"~{ev[0]:.0f} t, ~{ev[1]:.0f} m³"))
    out.append(("ship regional", f"~{rg[0]:.1f} t, ~{rg[1]:.0f} m³"))
    return out


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")        # MISSION.md uses ×, –, ≥, m³
    print("running scripts:")
    bad = run_all()
    with open(os.path.join(HERE, "MISSION.md"), encoding="utf-8") as fh:
        text = fh.read()
    print("\nMISSION.md vs the scripts:")
    missing = []
    for what, s in claims():
        ok = s in text
        print(f"  {'ok ' if ok else 'OUT'} {what:28s} {s}")
        if not ok:
            missing.append(what)
    if bad or missing:
        print(f"\nFAIL: {len(bad)} script error(s), {len(missing)} stale number(s) in MISSION.md")
        for s, err in bad:
            print(f"  {s}: {err[0]}")
        sys.exit(1)
    print("\nPASS: every script runs and MISSION.md matches them.")
