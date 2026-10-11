"""Counting the calls a naive recursion makes, rather than describing them."""

calls = {"n": 0}


def fib_counted(n):
    """The Fibonacci definition, with every entry counted."""
    calls["n"] += 1
    if n <= 1:
        return n
    return fib_counted(n - 1) + fib_counted(n - 2)


print(f"{'n':>4} {'F(n)':>8} {'calls':>10} {'calls/previous':>16}")
previous = None
for n in range(5, 27, 3):
    calls["n"] = 0
    value = fib_counted(n)
    ratio = "-" if previous is None else f"{calls['n'] / previous:.3f}"
    print(f"{n:>4} {value:>8} {calls['n']:>10} {ratio:>16}")
    previous = calls["n"]
print()
calls["n"] = 0
fib_counted(20)
print(f"F(20) costs {calls['n']} calls to produce one number.")
