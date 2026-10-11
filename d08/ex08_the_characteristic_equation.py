"""Turning a recurrence into a polynomial, and reading the roots off it."""
from dmkit.recur import characteristic_roots

cases = [
    ("a(n) = 3*a(n-1) - 2*a(n-2)", [3, -2], "x**2 - 3x + 2"),
    ("a(n) = a(n-1) + a(n-2)", [1, 1], "x**2 - x - 1"),
    ("a(n) = 5*a(n-1) - 6*a(n-2)", [5, -6], "x**2 - 5x + 6"),
    ("a(n) = 4*a(n-1) - 4*a(n-2)", [4, -4], "x**2 - 4x + 4"),
    ("a(n) = 6*a(n-1) - 8*a(n-2)", [6, -8], "x**2 - 6x + 8"),
    ("a(n) = 2*a(n-1) + 3*a(n-2)", [2, 3], "x**2 - 2x - 3"),
]
print(f"{'recurrence':>30} {'the equation':>16} {'roots':>34} {'kind':>10}")
for text, coefficients, equation in cases:
    roots = characteristic_roots(coefficients)
    kind = "repeated" if len(roots) == 1 else "distinct"
    shown = [str(r) if isinstance(r, int) or hasattr(r, "numerator")
             else f"{r:.6f}" for r in roots]
    print(f"{text:>30} {equation:>16} {str(shown):>34} {kind:>10}")
print()
p, q = 1, 1
roots = characteristic_roots([p, q])
print(f"the Fibonacci roots are {roots[0]:.9f} and {roots[1]:.9f}")
print(f"their product is {roots[0] * roots[1]:.9f} and their sum is "
      f"{roots[0] + roots[1]:.9f}")
print(f"the larger is the golden ratio Day 4 measured in a count of calls.")
