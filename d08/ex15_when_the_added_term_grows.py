"""An added term that is not a constant, and the case where the usual guess fails."""
from fractions import Fraction

from dmkit.recur import agrees_with, iterate

print("a(n) = 2*a(n-1) + n, a(0) = 0")
terms = iterate([2], [0], 14, lambda n: n)
print(f"   the terms: {terms[:10]}")
print()
print(f"{'guess':>26} {'first disagreement':>20}")
for name, guess in (("n", lambda n: n),
                    ("2**n", lambda n: 2 ** n),
                    ("2**(n+1) - n - 2", lambda n: 2 ** (n + 1) - n - 2)):
    where = agrees_with(guess, terms, tolerance=0)
    label = "none in 0..13" if where is None else f"at n = {where}"
    print(f"{name:>26} {label:>20}")
print()
print("a(n) = 2*a(n-1) + 2**n, a(0) = 1")
hard = iterate([2], [1], 12, lambda n: 2 ** n)
print(f"   the terms: {hard[:9]}")
print()
print(f"{'guess':>26} {'first disagreement':>20}")
for name, guess in (("2**n", lambda n: 2 ** n),
                    ("3 * 2**n", lambda n: 3 * 2 ** n),
                    ("(n + 1) * 2**n", lambda n: (n + 1) * 2 ** n)):
    where = agrees_with(guess, terms=hard, tolerance=0)
    label = "none in 0..11" if where is None else f"at n = {where}"
    print(f"{name:>26} {label:>20}")
