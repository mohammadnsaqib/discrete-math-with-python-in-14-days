"""The closed form of the oldest recurrence in the book, against two other opinions."""
from sympy import Function, Symbol, rsolve

from dmkit.recur import (agrees_with, characteristic_roots, closed_form, iterate,
                         solve_linear)

coefficients, initial = [1, 1], [0, 1]
terms = iterate(coefficients, initial, 40)
constants, roots = solve_linear(coefficients, initial)
formula = closed_form(constants, roots)

print(f"the roots are {roots[0]:.12f} and {roots[1]:.12f}")
print(f"the constants are {constants[0]:.12f} and {constants[1]:.12f}")
print()
print(f"{'n':>4} {'iterated':>12} {'closed form':>22} {'difference':>14}")
for n in (0, 1, 5, 10, 20, 30):
    print(f"{n:>4} {terms[n]:>12} {formula(n):>22.6f} "
          f"{abs(formula(n) - terms[n]):>14.9f}")
print()
where = agrees_with(formula, terms, tolerance=1e-9)
print(f"first disagreement beyond one part in a billion: {where}")
print()
n = Symbol("n", integer=True)
a = Function("a")
solved = rsolve(a(n) - a(n - 1) - a(n - 2), a(n), {a(0): 0, a(1): 1})
print(f"SymPy solves the same recurrence to:")
print(f"   {solved}")
print(f"and at n = 30 that gives {int(solved.subs(n, 30))}, "
      f"against {terms[30]} by iteration.")
