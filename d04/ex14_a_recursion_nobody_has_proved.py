"""One recursion whose termination has never been proved, next to ones that have."""
from dmkit.induct import collatz_steps

print(f"{'n':>6} {'steps to 1':>12} {'highest value on the way':>26}")
for n in (6, 7, 27, 97, 871, 6171):
    peak, m = n, n
    while m != 1:
        m = m // 2 if m % 2 == 0 else 3 * m + 1
        peak = max(peak, m)
    print(f"{n:>6} {collatz_steps(n):>12} {peak:>26}")
print()
worst = max(range(1, 10000), key=lambda n: collatz_steps(n) or 0)
print(f"in 1..9999 the longest run belongs to {worst}, at {collatz_steps(worst)} "
      f"steps.")
unfinished = [n for n in range(1, 10000) if collatz_steps(n) is None]
print(f"values in 1..9999 that did not reach 1 within 1000 steps: {unfinished}")
