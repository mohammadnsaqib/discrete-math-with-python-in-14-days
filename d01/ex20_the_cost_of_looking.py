"""Where exhaustive checking stops being possible, measured rather than asserted."""
import time

from dmkit.logic import is_tautology


def best_of(fn, repeats=2):
    """The shortest of several runs, which is the only reproducible one.

    A single wall-clock reading of a short operation measures whatever else the machine
    was doing as well. The shortest run is the least interrupted.
    """
    best = float("inf")
    for _ in range(repeats):
        t0 = time.perf_counter()
        fn()
        best = min(best, time.perf_counter() - t0)
    return best


def always_true(**kwargs):
    """A tautology on any variables, so every row is visited and none is skipped."""
    return True


print(f"{'variables':>11} {'rows':>14} {'seconds':>11} {'ratio':>8}")
# The table starts at 12 and not at 2. Below a few thousand rows the reading is
# mostly the cost of starting the loop, and the ratio column then measures that
# rather than the doubling it exists to show.
times, sizes = [], (12, 14, 16, 18, 20)
prev = None
for n in sizes:
    names = [f"x{i}" for i in range(n)]
    t = best_of(lambda names=names: is_tautology(always_true, names))
    ratio = "" if prev is None else f"{t / prev:.2f}"
    print(f"{n:>11} {2 ** n:>14,} {t:>11.5f} {ratio:>8}")
    times.append(t)
    prev = t
print()
per_row = times[-1] / 2 ** sizes[-1]
print(f"each row costs about {per_row * 1e9:.0f} nanoseconds at this size")
for n in (24, 32, 40):
    seconds = per_row * 2 ** n
    if seconds < 3600:
        unit = f"{seconds:.0f} seconds"
    elif seconds < 86400:
        unit = f"{seconds / 3600:.1f} hours"
    elif seconds < 31557600:
        unit = f"{seconds / 86400:.0f} days"
    else:
        unit = f"{seconds / 31557600:.0f} years"
    print(f"  {n} variables would take about {unit}")
