"""Three words that describe a recurrence, and what each of them rules out."""
from dmkit.recur import iterate

rows = [
    ("a(n) = 5*a(n-1)", 1, True, True, [5], [1], None),
    ("a(n) = a(n-1) + a(n-2)", 2, True, True, [1, 1], [0, 1], None),
    ("a(n) = 2*a(n-1) + 1", 1, True, False, [2], [0], lambda n: 1),
    ("a(n) = a(n-1) + n", 1, True, False, [1], [0], lambda n: n),
    ("a(n) = 3*a(n-1) - 2*a(n-2) + 2**n", 2, True, False, [3, -2], [0, 1],
     lambda n: 2 ** n),
]
print(f"{'recurrence':>36} {'order':>6} {'linear':>7} {'homogeneous':>12} "
      f"{'first six terms':>30}")
for text, order, linear, homogeneous, coefficients, initial, forcing in rows:
    terms = iterate(coefficients, initial, 6, forcing)
    print(f"{text:>36} {order:>6} {str(linear):>7} {str(homogeneous):>12} "
          f"{str(terms):>30}")
