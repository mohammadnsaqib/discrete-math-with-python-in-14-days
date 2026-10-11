"""Problem 3.28: the doubling, and where building the power set stops being possible."""
import time

from dmkit.sets import power_set


def best_of(fn, repeats=3):
    """The shortest of several runs, which is the only reproducible one."""
    best = float("inf")
    for _ in range(repeats):
        t0 = time.perf_counter()
        fn()
        best = min(best, time.perf_counter() - t0)
    return best


print(f"{'members':>9} {'subsets':>12} {'built':>10} {'seconds':>10} {'ratio':>8}")
prev = None
# Starts at 12: below a few thousand subsets the reading is mostly the cost of
# starting the loop, and the ratio column then measures that instead.
for n in (12, 14, 16, 18, 20):
    base = set(range(1, n + 1))
    t = best_of(lambda base=base: power_set(base))
    built = len(power_set(base))
    ratio = "" if prev is None else f"{t / prev:.2f}"
    print(f"{n:>9} {2 ** n:>12,} {built:>10,} {t:>10.5f} {ratio:>8}")
    prev = t
print()
per = prev / 2 ** 20
print(f"each subset costs about {per * 1e9:.0f} nanoseconds at this size")
for n in (30, 40, 64):
    seconds = per * 2 ** n
    if seconds < 3600:
        unit = f"{seconds / 60:.0f} minutes"
    elif seconds < 86400:
        unit = f"{seconds / 3600:.1f} hours"
    elif seconds < 31557600:
        unit = f"{seconds / 86400:.0f} days"
    else:
        unit = f"{seconds / 31557600:.3g} years"
    print(f"   {n} members would take about {unit} to enumerate")
