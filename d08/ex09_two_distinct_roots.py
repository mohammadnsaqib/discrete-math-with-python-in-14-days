"""A second-order recurrence solved, and the closed form checked against the iteration.
"""
from dmkit.recur import agrees_with, closed_form, iterate, solve_linear

cases = [
    ("a(n) = 3*a(n-1) - 2*a(n-2), a(0)=1, a(1)=3", [3, -2], [1, 3]),
    ("a(n) = 5*a(n-1) - 6*a(n-2), a(0)=1, a(1)=1", [5, -6], [1, 1]),
    ("a(n) = 6*a(n-1) - 8*a(n-2), a(0)=2, a(1)=6", [6, -8], [2, 6]),
    ("a(n) = 2*a(n-1) + 3*a(n-2), a(0)=1, a(1)=3", [2, 3], [1, 3]),
]
print(f"{'recurrence':>44} {'roots':>14} {'constants':>18} {'disagreement':>16}")
for text, coefficients, initial in cases:
    constants, roots = solve_linear(coefficients, initial)
    formula = closed_form(constants, roots)
    terms = iterate(coefficients, initial, 40)
    where = agrees_with(formula, terms, tolerance=0)
    label = "none in 0..39" if where is None else f"at n = {where}"
    print(f"{text:>44} {str([str(r) for r in roots]):>14} "
          f"{str([str(c) for c in constants]):>18} {label:>16}")
print()
coefficients, initial = [3, -2], [1, 3]
constants, roots = solve_linear(coefficients, initial)
formula = closed_form(constants, roots)
print(f"the closed form is {constants[0]} * {roots[0]}**n + "
      f"{constants[1]} * {roots[1]}**n")
terms = iterate(coefficients, initial, 21)
print(f"{'n':>4} {'iterated':>12} {'closed form':>14} {'agree':>7}")
for n in (0, 1, 2, 10, 20):
    print(f"{n:>4} {terms[n]:>12} {formula(n):>14} {str(terms[n] == formula(n)):>7}")
