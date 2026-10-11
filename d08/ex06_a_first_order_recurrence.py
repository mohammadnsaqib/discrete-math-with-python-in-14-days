"""The simplest linear recurrence, solved rather than guessed."""
from fractions import Fraction

from dmkit.recur import agrees_with, closed_form, iterate, solve_linear

cases = [([2], [1]), ([3], [4]), ([5], [2]), ([1], [7])]
print(f"{'recurrence':>26} {'root':>6} {'constant':>10} {'closed form':>18} "
      f"{'first disagreement':>20}")
for coefficients, initial in cases:
    constants, roots = solve_linear(coefficients, initial)
    formula = closed_form(constants, roots)
    terms = iterate(coefficients, initial, 40)
    where = agrees_with(formula, terms, tolerance=0)
    label = "none in 0..39" if where is None else f"at n = {where}"
    text = f"a(n) = {coefficients[0]}*a(n-1), a(0) = {initial[0]}"
    print(f"{text:>26} {str(roots[0]):>6} {str(constants[0]):>10} "
          f"{f'{constants[0]} * {roots[0]}**n':>18} {label:>20}")
print()
coefficients, initial = [3], [4]
constants, roots = solve_linear(coefficients, initial)
formula = closed_form(constants, roots)
print(f"{'n':>4} {'iterated':>12} {'closed form':>14} {'agree':>7}")
for n in (0, 1, 5, 10, 20):
    terms = iterate(coefficients, initial, n + 1)
    print(f"{n:>4} {terms[n]:>12} {formula(n):>14} {str(terms[n] == formula(n)):>7}")
