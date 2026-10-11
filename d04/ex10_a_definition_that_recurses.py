"""A recursive definition is an induction written as code."""
from dmkit.induct import check_identity, closed_sum, sum_to


def sum_recursive(n):
    """1 + 2 + ... + n, defined the way an induction is stated.

    The base case of the definition is the base case of the proof, and the last line is
    the step. Nothing was translated: the two are the same two sentences.
    """
    if n == 0:
        return 0
    return sum_recursive(n - 1) + n


print(f"{'n':>4} {'recursive':>10} {'by adding':>10} {'closed form':>12} {'agree':>6}")
for n in (0, 1, 5, 10, 50, 100):
    a, b, c = sum_recursive(n), sum_to(n), closed_sum(n)
    print(f"{n:>4} {a:>10} {b:>10} {c:>12} {str(a == b == c):>6}")
print()
bad = check_identity(sum_recursive, closed_sum, 0, 900)
print(f"first disagreement between the recursion and the closed form in 0..899: {bad}")
