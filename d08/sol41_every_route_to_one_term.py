"""Problem 8.28: term fifty of one recurrence, reached four ways."""
from sympy import Function, Symbol, nsimplify, rsolve, simplify

from dmkit.induct import best_of
from dmkit.recur import (agrees_with, closed_form, iterate, multiply_series,
                         solve_linear)

coefficients, initial, target = [3, -2], [2, 5], 50
terms = iterate(coefficients, initial, target + 1)
constants, roots = solve_linear(coefficients, initial)
formula = closed_form(constants, roots)

n = Symbol("n", integer=True)
a = Function("a")
solved = simplify(rsolve(a(n) - 3 * a(n - 1) + 2 * a(n - 2), a(n), {a(0): 2, a(1): 5}))

print(f"a(n) = 3*a(n-1) - 2*a(n-2), a(0) = 2, a(1) = 5")
print(f"   the first eight terms : {terms[:8]}")
print(f"   the roots             : {[str(r) for r in roots]}")
print(f"   the closed form       : {constants[0]} * {roots[0]}**n + "
      f"{constants[1]} * {roots[1]}**n")
print(f"   SymPy gives           : {solved}")
print()
print(f"{'route':>26} {'term 50':>22} {'agrees with the iteration':>27}")
print(f"{'iteration':>26} {terms[target]:>22} {'-':>27}")
print(f"{'the closed form':>26} {formula(target):>22} "
      f"{str(formula(target) == terms[target]):>27}")
print(f"{'SymPy':>26} {int(nsimplify(solved.subs(n, target))):>22} "
      f"{str(int(nsimplify(solved.subs(n, target))) == terms[target]):>27}")
running = multiply_series([1] * (target + 1), terms, target + 1)
print(f"{'running totals, term 50':>26} {running[target]:>22} {'-':>27}")
print()
where = agrees_with(formula, terms, tolerance=0)
print(f"first disagreement between the closed form and the iteration: {where}")
print()
big = iterate(coefficients, initial, 5001)
value = formula(5000)
walked = best_of(lambda: iterate(coefficients, initial, 5001), 5)
direct = best_of(lambda: formula(5000), 5)
print(f"{'route':>26} {'seconds for term 5000':>23} {'times the faster':>18}")
print(f"{'iteration':>26} {walked:>23.6f} {walked / direct:>18.1f}")
print(f"{'the closed form':>26} {direct:>23.6f} {1.0:>18.1f}")
print(f"and the two agree at term 5000: {value == big[5000]}")
