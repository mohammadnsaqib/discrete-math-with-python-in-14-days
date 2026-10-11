"""One decorator, and a count of calls that stops growing like a Fibonacci number."""
from functools import lru_cache

plain_calls = {"n": 0}
memo_calls = {"n": 0}


def fib_plain(n):
    """The definition, recomputing everything it has already computed."""
    plain_calls["n"] += 1
    if n <= 1:
        return n
    return fib_plain(n - 1) + fib_plain(n - 2)


@lru_cache(maxsize=None)
def fib_remembered(n):
    """The SAME definition, with each value computed once and kept."""
    memo_calls["n"] += 1
    if n <= 1:
        return n
    return fib_remembered(n - 1) + fib_remembered(n - 2)


print(f"{'n':>4} {'F(n)':>10} {'plain calls':>13} {'remembered':>12} {'ratio':>10}")
for n in range(5, 31, 5):
    plain_calls["n"] = 0
    memo_calls["n"] = 0
    fib_remembered.cache_clear()
    value = fib_plain(n)
    fib_remembered(n)
    ratio = plain_calls["n"] / memo_calls["n"]
    print(f"{n:>4} {value:>10} {plain_calls['n']:>13} {memo_calls['n']:>12} "
          f"{ratio:>10.1f}")
