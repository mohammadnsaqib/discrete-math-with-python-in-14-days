"""A recurrence defines each term from earlier ones, and nothing else."""
from dmkit.recur import iterate

recurrences = [
    ("a(n) = 2*a(n-1), a(0) = 1", [2], [1], None),
    ("a(n) = a(n-1) + 3, a(0) = 5", [1], [5], lambda n: 3),
    ("a(n) = a(n-1) + a(n-2), a(0) = 0, a(1) = 1", [1, 1], [0, 1], None),
    ("a(n) = 2*a(n-1) + 1, a(0) = 0", [2], [0], lambda n: 1),
    ("a(n) = 3*a(n-1) - 2*a(n-2), a(0) = 1, a(1) = 3", [3, -2], [1, 3], None),
]
print(f"{'recurrence':>46} {'the first eight terms':>34}")
for text, coefficients, initial, forcing in recurrences:
    terms = iterate(coefficients, initial, 8, forcing)
    print(f"{text:>46} {str(terms):>34}")
