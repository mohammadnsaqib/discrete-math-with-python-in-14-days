"""Problem 8.25: one routine that solves a linear homogeneous recurrence of order one or
two."""
from dmkit.recur import (agrees_with, characteristic_roots, closed_form, iterate,
                         solve_linear, solve_repeated)


def _short(value):
    """A root or constant printed in a fixed width, exact when it can be."""
    return str(value) if hasattr(value, "numerator") else f"{value:.6f}"


def _as_text(coefficients):
    """The recurrence written out, with the sign of the second coefficient carried."""
    text = f"a(n) = {coefficients[0]}*a(n-1)"
    if len(coefficients) > 1:
        sign = "+" if coefficients[1] >= 0 else "-"
        text += f" {sign} {abs(coefficients[1])}*a(n-2)"
    return text


def solve(coefficients, initial):
    """The closed form, the shape used, and where it first differs from the iteration.
    """
    roots = characteristic_roots(coefficients)
    if len(coefficients) == 2 and len(roots) == 1:
        constants, roots = solve_repeated(coefficients, initial)
        formula = closed_form(constants, roots, repeated=True)
        shape = "(A + B*n) * r**n"
    else:
        constants, roots = solve_linear(coefficients, initial)
        formula = closed_form(constants, roots)
        shape = "A * r**n" if len(constants) == 1 else "A * r**n + B * s**n"
    terms = iterate(coefficients, initial, 40)
    exact = all(hasattr(r, "numerator") for r in roots)
    where = agrees_with(formula, terms, tolerance=0 if exact else 1e-9)
    return {"roots": [_short(r) for r in roots],
            "constants": [_short(c) for c in constants],
            "shape": shape, "exact": exact, "disagreement": where}


cases = [([2], [1]), ([3], [5]), ([3, -2], [1, 3]), ([5, -6], [1, 1]),
         ([4, -4], [1, 6]), ([6, -9], [2, 9]), ([1, 1], [0, 1]), ([2, -1], [3, 5])]
print(f"{'recurrence':>32} {'shape':>20} {'exact':>6} {'disagreement':>14}")
for coefficients, initial in cases:
    r = solve(coefficients, initial)
    label = "none in 0..39" if r["disagreement"] is None else f"at {r['disagreement']}"
    print(f"{_as_text(coefficients):>32} {r['shape']:>20} {str(r['exact']):>6} "
          f"{label:>14}")
print()
print(f"{'recurrence':>32} {'roots':>24} {'constants':>30}")
for coefficients, initial in cases:
    r = solve(coefficients, initial)
    print(f"{_as_text(coefficients):>32} {str(r['roots']):>26} "
          f"{str(r['constants']):>30}")
