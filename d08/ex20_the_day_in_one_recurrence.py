"""One recurrence, taken through every route the day has built."""
from sympy import Function, Symbol, rsolve

from dmkit.recur import (agrees_with, characteristic_roots, closed_form, iterate,
                         multiply_series, solve_linear)

coefficients, initial = [5, -6], [2, 5]
terms = iterate(coefficients, initial, 30)
roots = characteristic_roots(coefficients)
constants, roots = solve_linear(coefficients, initial)
formula = closed_form(constants, roots)

print(f"a(n) = 5*a(n-1) - 6*a(n-2), a(0) = 2, a(1) = 5")
print(f"   the first eight terms : {terms[:8]}")
print(f"   the roots             : {[str(r) for r in roots]}")
print(f"   the constants         : {[str(c) for c in constants]}")
print(f"   the closed form       : {constants[0]} * {roots[0]}**n + "
      f"{constants[1]} * {roots[1]}**n")
print()
where = agrees_with(formula, terms, tolerance=0)
print(f"first disagreement with the iteration in 0..29: {where}")
print()
n = Symbol("n", integer=True)
a = Function("a")
solved = rsolve(a(n) - 5 * a(n - 1) + 6 * a(n - 2), a(n), {a(0): 2, a(1): 5})
print(f"SymPy solves it to: {solved}")
print(f"at n = 25 SymPy gives {int(solved.subs(n, 25))}")
print(f"and the iteration gives {terms[25]}")
print(f"and the closed form gives {formula(25)}")
print()
ones = [1] * 30
running = multiply_series(ones, terms, 8)
print(f"{'n':>4} {'a(n)':>8} {'running total':>15}")
for k in range(6):
    print(f"{k:>4} {terms[k]:>8} {running[k]:>15}")
