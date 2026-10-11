"""The counted coefficients against an expansion done by a computer algebra system."""
from sympy import Poly, expand, symbols

from dmkit.combin import expand_binomial

a, b = symbols("a b")

print(f"{'n':>4} {'counted':>34} {'expanded by SymPy':>34} {'agree':>7}")
for n in range(0, 8):
    counted = expand_binomial(n)
    poly = Poly(expand((a + b) ** n), a, b)
    oracle = [int(poly.coeff_monomial(a ** (n - k) * b ** k)) for k in range(n + 1)]
    print(f"{n:>4} {str(counted):>34} {str(oracle):>34} {str(counted == oracle):>7}")
print()
print(f"(a + b)**4 expanded: {expand((a + b) ** 4)}")
