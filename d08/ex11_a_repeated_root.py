"""When the characteristic equation has one root twice, the usual shape stops working.
"""
from dmkit.recur import agrees_with, characteristic_roots, iterate

coefficients, initial = [4, -4], [1, 6]
roots = characteristic_roots(coefficients)
terms = iterate(coefficients, initial, 12)

print(f"a(n) = 4*a(n-1) - 4*a(n-2), a(0) = 1, a(1) = 6")
print(f"the characteristic equation is x**2 - 4x + 4, whose roots are "
      f"{[str(r) for r in roots]}")
print(f"the first twelve terms: {terms}")
print()
print("the usual shape is A*r**n + B*s**n with "
      "two DIFFERENT roots. Here r and s are the")
print("same number, so that shape collapses to (A + B) * 2**n, which is one constant")
print("wearing two names. One constant cannot match two starting terms.")
print()
print(f"{'guess':>22} {'at n=0':>8} {'at n=1':>8} {'first disagreement':>20}")
for name, guess in (("1 * 2**n", lambda n: 1 * 2 ** n),
                    ("3 * 2**n", lambda n: 3 * 2 ** n),
                    ("(1 + 2*n) * 2**n", lambda n: (1 + 2 * n) * 2 ** n)):
    where = agrees_with(guess, terms, tolerance=0)
    label = "none in 0..11" if where is None else f"at n = {where}"
    print(f"{name:>22} {guess(0):>8} {guess(1):>8} {label:>20}")
