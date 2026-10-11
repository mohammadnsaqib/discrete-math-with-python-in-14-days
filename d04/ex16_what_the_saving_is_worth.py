"""The call counts said the recursion was expensive. The clock is asked to agree."""
from dmkit.induct import best_of, fib_iterative, fib_memo, fib_recursive

N = 27

# THE FAST METHODS ARE TIMED IN BATCHES. A single memoised run finishes in a few
# microseconds, which is near the floor of what the clock can resolve, so each batch is
# made long enough to be measured and the time is divided back down.
BATCH = 2000


def run_plain():
    """One run of the plain recursion, which is already long enough to time."""
    fib_recursive(N)


def run_memo():
    """A batch of cold runs: the cache is cleared so nothing is inherited from the run
    before."""
    for _ in range(BATCH):
        fib_memo.cache_clear()
        fib_memo(N)


def run_iterative():
    """A batch of iterative runs."""
    for _ in range(BATCH):
        fib_iterative(N)


print(f"F({N}) = {fib_iterative(N)}")
print()
rows = [("plain recursion", run_plain, 1),
        ("memoised recursion", run_memo, BATCH),
        ("iterative", run_iterative, BATCH)]
print(f"{'method':>20} {'batch':>7} {'best of 5, seconds':>20} {'per run':>12} "
      f"{'times fastest':>15}")
measured = [(name, best_of(fn, 5), batch) for name, fn, batch in rows]
per_run = [(name, t / batch) for name, t, batch in measured]
floor = min(t for _, t in per_run)
for (name, total, batch), (_, each) in zip(measured, per_run):
    print(f"{name:>20} {batch:>7} {total:>20.6f} {each:>12.9f} {each / floor:>15.1f}")
print()
plain_calls = 2 * fib_iterative(N + 1) - 1
print(f"the plain recursion enters itself {plain_calls} times to compute F({N}).")
print(f"the memoised one enters itself {N + 1} times, "
      f"{plain_calls / (N + 1):.0f} times fewer.")
