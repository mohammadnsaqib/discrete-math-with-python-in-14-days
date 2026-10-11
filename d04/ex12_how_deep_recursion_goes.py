"""Every recursion in Python runs on a stack with a hard floor under it."""
import sys


def depth_recursive(n):
    """Count down to zero, one frame per step."""
    if n == 0:
        return 0
    return depth_recursive(n - 1) + 1


print(f"the interpreter's recursion limit is {sys.getrecursionlimit()}")
print()
print(f"{'depth asked':>12} {'result':>28}")
for n in (10, 100, 900, 2000, 20000):
    try:
        print(f"{n:>12} {depth_recursive(n):>28}")
    except RecursionError:
        print(f"{n:>12} {'RecursionError: limit reached':>28}")
print()


def depth_iterative(n):
    """The same count, with no frames at all."""
    total = 0
    for _ in range(n):
        total += 1
    return total


print(f"the same count at 1000000, computed iteratively: {depth_iterative(1000000)}")
