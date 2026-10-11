"""A conditional claim can be confirmed by a range that never tested it."""
from dmkit.proof import direct_check, divides

claims = [
    ("if 6 divides n then 3 divides n",
     lambda n: divides(6, n), lambda n: divides(3, n), range(1, 61)),
    ("if n is above 1000 then n is negative",
     lambda n: n > 1000, lambda n: n < 0, range(1, 61)),
    ("if n divides 7 and n > 1 then n is 7",
     lambda n: divides(n, 7) and n > 1, lambda n: n == 7, range(1, 61)),
]
print(f"{'claim':>36} {'tested':>7} {'failed':>7} {'skipped':>8} {'what it shows':>26}")
for text, hyp, con, dom in claims:
    r = direct_check(hyp, con, dom)
    if r["tested"] == 0:
        verdict = "nothing: never tested"
    elif r["failures"]:
        verdict = f"REFUTED at {r['first_failure']}"
    else:
        plural = "member" if r["tested"] == 1 else "members"
        verdict = f"held on {r['tested']} {plural}"
    print(f"{text:>36} {r['tested']:>7} {r['failures']:>7} {r['vacuous']:>8} "
          f"{verdict:>26}")
