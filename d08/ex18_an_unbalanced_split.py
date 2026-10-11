"""A split that does not divide evenly, and what it costs."""
from functools import lru_cache
from math import log2


@lru_cache(maxsize=None)
def even_split(n):
    """T(n) = 2*T(n/2) + n, rounded so that every size is reachable."""
    if n <= 1:
        return 1
    return even_split(n // 2) + even_split(n - n // 2) + n


@lru_cache(maxsize=None)
def uneven_split(n):
    """T(n) = T(n/3) + T(2n/3) + n, which the master theorem does not cover.

    THE BASE CASE IS 2, NOT 1. At n = 2 the smaller part is 2 // 3, which is 0, so the
    larger part is 2 again and the recursion never shrinks. A base case set one step too
    low turns a correct recurrence into an infinite one, and the interpreter is the only
    thing that says so.
    """
    if n <= 2:
        return n
    return uneven_split(n // 3) + uneven_split(n - n // 3) + n


def worst_split(n):
    """T(n) = T(1) + T(n-1) + n, the split that takes one item off at a time.

    Written as a loop rather than a recursion: at n = 4096 the recursion would need 4096
    frames, and Day 4 measured where the interpreter stops handing them out.
    """
    total = 1
    for k in range(2, n + 1):
        total += 1 + k
    return total


print(f"{'size':>8} {'even split':>12} {'one third':>12} {'one item':>12} "
      f"{'n log2 n':>12}")
for size in (16, 64, 256, 1024, 4096):
    print(f"{size:>8} {even_split(size):>12} {uneven_split(size):>12} "
          f"{worst_split(size):>12} {size * log2(size):>12.0f}")
print()
print(f"{'size':>8} {'even / n log n':>16} {'third / n log n':>17} "
      f"{'one item / n**2':>17}")
for size in (64, 256, 1024, 4096):
    predicted = size * log2(size)
    print(f"{size:>8} {even_split(size) / predicted:>16.4f} "
          f"{uneven_split(size) / predicted:>17.4f} "
          f"{worst_split(size) / size ** 2:>17.4f}")
