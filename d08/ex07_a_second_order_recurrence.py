"""Two earlier terms instead of one, and why the first-order answer stops working."""
from dmkit.recur import agrees_with, iterate

coefficients, initial = [3, -2], [1, 3]
terms = iterate(coefficients, initial, 12)
print(f"a(n) = 3*a(n-1) - 2*a(n-2), a(0) = 1, a(1) = 3")
print(f"the first twelve terms: {terms}")
print()
print(f"{'guess':>18} {'first disagreement':>20}")
for name, guess in (("3**n", lambda n: 3 ** n),
                    ("2**n", lambda n: 2 ** n),
                    ("2 * 2**n", lambda n: 2 * 2 ** n),
                    ("2 * 2**n - 1", lambda n: 2 * 2 ** n - 1)):
    where = agrees_with(guess, terms, tolerance=0)
    label = "none in 0..11" if where is None else f"at n = {where}"
    print(f"{name:>18} {label:>20}")
print()
print(f"{'n':>4} {'a(n)':>10} {'a(n)/a(n-1)':>14}")
for n in range(1, 9):
    print(f"{n:>4} {terms[n]:>10} {terms[n] / terms[n - 1]:>14.6f}")
