"""Cancelling is not always allowed, and the multiplication table shows when."""
from dmkit.crypto import mod_table

for m in (5, 6):
    print(f"multiplication modulo {m}:")
    table = mod_table(m, lambda a, b: a * b)
    print("    " + " ".join(f"{b:>3}" for b in range(m)))
    for a, row in enumerate(table):
        print(f"{a:>3} " + " ".join(f"{v:>3}" for v in row))
    zeros = [(a, b) for a in range(1, m) for b in range(1, m) if a * b % m == 0]
    print(f"   non-zero pairs whose product is 0: {zeros}")
    print()
print(f"{'m':>4} {'a':>4} {'b':>4} {'c':>4} {'a*b mod m':>11} {'a*c mod m':>11} "
      f"{'same product':>14} {'b = c':>7} {'cancelling safe':>17}")
for m, a, b, c in ((6, 2, 1, 4), (6, 3, 1, 3), (5, 2, 1, 4), (5, 2, 3, 3),
                   (12, 4, 2, 5)):
    same_product = a * b % m == a * c % m
    print(f"{m:>4} {a:>4} {b:>4} {c:>4} {a * b % m:>11} {a * c % m:>11} "
          f"{str(same_product):>14} {str(b == c):>7} "
          f"{str(not same_product or b == c):>17}")
