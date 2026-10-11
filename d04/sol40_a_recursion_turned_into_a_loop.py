"""Problem 4.27: three recursions rewritten as loops, and the two versions compared."""
from dmkit.induct import hanoi


def sum_rec(n):
    """1 + 2 + ... + n, by recursion."""
    return 0 if n == 0 else sum_rec(n - 1) + n


def sum_loop(n):
    """The same, by a loop that carries the running total."""
    total = 0
    for k in range(1, n + 1):
        total += k
    return total


def fact_rec(n):
    """n!, by recursion."""
    return 1 if n == 0 else n * fact_rec(n - 1)


def fact_loop(n):
    """The same, by a loop that carries the running product."""
    result = 1
    for k in range(2, n + 1):
        result *= k
    return result


def hanoi_loop(n):
    """Every move for n discs, produced by a stack instead of the call stack.

    THE STACK IS THE POINT. A recursion keeps its pending work in the interpreter's
    frames, which is why it runs out of them. Written this way the pending work is an
    ordinary list, and the only limit is memory.
    """
    moves = []
    pending = [(n, "A", "C", "B", False)]
    while pending:
        k, src, dst, spare, ready = pending.pop()
        if k == 0:
            continue
        if ready:
            moves.append((k, src, dst))
        else:
            pending.append((k - 1, spare, dst, src, False))
            pending.append((k, src, dst, spare, True))
            pending.append((k - 1, src, spare, dst, False))
    return moves


print(f"{'routine':>14} {'n':>5} {'recursive':>24} {'loop':>24} {'agree':>6}")
for n in (0, 1, 6, 20, 60):
    a, b = sum_rec(n), sum_loop(n)
    print(f"{'sum to n':>14} {n:>5} {a:>24} {b:>24} {str(a == b):>6}")
for n in (0, 1, 6, 12, 20):
    a, b = fact_rec(n), fact_loop(n)
    print(f"{'factorial':>14} {n:>5} {a:>24} {b:>24} {str(a == b):>6}")
print()
disagree = [n for n in range(0, 13) if hanoi(n) != hanoi_loop(n)]
print(f"disc counts 0..12 where the two towers routines differ: {disagree}")
print(f"the moves for 3 discs, from the loop: {hanoi_loop(3)}")
