"""A recurrence with something added that does not involve an earlier term."""
from dmkit.recur import agrees_with, iterate

coefficients, initial = [2], [0]
terms = iterate(coefficients, initial, 16, lambda n: 1)
homogeneous = iterate(coefficients, [1], 16)

print(f"a(n) = 2*a(n-1) + 1, a(0) = 0")
print(f"   the terms          : {terms[:10]}")
print(f"a(n) = 2*a(n-1), a(0) = 1")
print(f"   the terms          : {homogeneous[:10]}")
print(f"   the difference     : {[t - h for t, h in zip(terms, homogeneous)][:10]}")
print()
print(f"{'guess':>18} {'first disagreement':>20}")
for name, guess in (("2**n", lambda n: 2 ** n),
                    ("2**n - 1", lambda n: 2 ** n - 1),
                    ("2**(n+1) - 2", lambda n: 2 ** (n + 1) - 2)):
    where = agrees_with(guess, terms, tolerance=0)
    label = "none in 0..15" if where is None else f"at n = {where}"
    print(f"{name:>18} {label:>20}")
