"""Problem 8.26: the book's solver against SymPy, on eight recurrences."""
from sympy import Function, Symbol, nsimplify, rsolve, simplify

from dmkit.recur import (characteristic_roots, closed_form, iterate, solve_linear,
                         solve_repeated)

n = Symbol("n", integer=True)
a = Function("a")

cases = [
    ([2], [1], a(n) - 2 * a(n - 1)),
    ([3], [5], a(n) - 3 * a(n - 1)),
    ([3, -2], [1, 3], a(n) - 3 * a(n - 1) + 2 * a(n - 2)),
    ([5, -6], [1, 1], a(n) - 5 * a(n - 1) + 6 * a(n - 2)),
    ([4, -4], [1, 6], a(n) - 4 * a(n - 1) + 4 * a(n - 2)),
    ([6, -9], [2, 9], a(n) - 6 * a(n - 1) + 9 * a(n - 2)),
    ([1, 1], [0, 1], a(n) - a(n - 1) - a(n - 2)),
    ([2, -1], [3, 5], a(n) - 2 * a(n - 1) + a(n - 2)),
]
print(f"{'recurrence':>26} {'SymPy gives':>34} {'at n=20, SymPy':>18} "
      f"{'iterated':>12} {'agree':>7}")
for coefficients, initial, equation in cases:
    known = {a(k): v for k, v in enumerate(initial)}
    solved = simplify(rsolve(equation, a(n), known))
    terms = iterate(coefficients, initial, 21)
    value = int(nsimplify(solved.subs(n, 20)))
    text = f"a(n) = {coefficients[0]}*a(n-1)"
    if len(coefficients) > 1:
        sign = "+" if coefficients[1] >= 0 else "-"
        text += f" {sign} {abs(coefficients[1])}*a(n-2)"
    print(f"{text:>26} {str(solved):>34} {value:>18} {terms[20]:>12} "
          f"{str(value == terms[20]):>7}")
