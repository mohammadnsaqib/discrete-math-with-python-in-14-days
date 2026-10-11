"""The right shape for a repeated root, and the constants solved for it."""
from dmkit.recur import agrees_with, closed_form, iterate, solve_repeated

cases = [
    ("a(n) = 4*a(n-1) - 4*a(n-2), a(0)=1, a(1)=6", [4, -4], [1, 6]),
    ("a(n) = 6*a(n-1) - 9*a(n-2), a(0)=1, a(1)=3", [6, -9], [1, 3]),
    ("a(n) = 6*a(n-1) - 9*a(n-2), a(0)=2, a(1)=9", [6, -9], [2, 9]),
    ("a(n) = 2*a(n-1) - a(n-2), a(0)=3, a(1)=5", [2, -1], [3, 5]),
]
print(f"{'recurrence':>44} {'root':>6} {'A':>6} {'B':>6} {'disagreement':>16}")
for text, coefficients, initial in cases:
    constants, roots = solve_repeated(coefficients, initial)
    formula = closed_form(constants, roots, repeated=True)
    terms = iterate(coefficients, initial, 40)
    where = agrees_with(formula, terms, tolerance=0)
    label = "none in 0..39" if where is None else f"at n = {where}"
    print(f"{text:>44} {str(roots[0]):>6} {str(constants[0]):>6} "
          f"{str(constants[1]):>6} {label:>16}")
print()
coefficients, initial = [4, -4], [1, 6]
constants, roots = solve_repeated(coefficients, initial)
formula = closed_form(constants, roots, repeated=True)
terms = iterate(coefficients, initial, 21)
print(f"the closed form is ({constants[0]} + {constants[1]}*n) * {roots[0]}**n")
print(f"{'n':>4} {'iterated':>14} {'closed form':>16} {'agree':>7}")
for n in (0, 1, 2, 10, 20):
    print(f"{n:>4} {terms[n]:>14} {formula(n):>16} {str(terms[n] == formula(n)):>7}")
