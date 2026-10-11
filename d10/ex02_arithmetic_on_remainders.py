"""Adding and multiplying remainders gives the remainder of the sum and the product."""
from dmkit.crypto import mod_table

m = 5
print(f"addition modulo {m}:")
table = mod_table(m, lambda a, b: a + b)
print("    " + " ".join(f"{b:>3}" for b in range(m)))
for a, row in enumerate(table):
    print(f"{a:>3} " + " ".join(f"{v:>3}" for v in row))
print()
print(f"multiplication modulo {m}:")
table = mod_table(m, lambda a, b: a * b)
print("    " + " ".join(f"{b:>3}" for b in range(m)))
for a, row in enumerate(table):
    print(f"{a:>3} " + " ".join(f"{v:>3}" for v in row))
print()
bad = [(a, b, m) for m in range(2, 20) for a in range(-30, 31) for b in range(-30, 31)
       if (a + b) % m != (a % m + b % m) % m or (a * b) % m != (a % m * (b % m)) % m]
print(f"triples where reducing first changed the answer: {len(bad)}")
print()
print(f"{'expression':>34} {'the long way':>16} {'reducing first':>16} {'agree':>7}")
for a, b, m in ((123456, 789012, 97), (2 ** 20, 3 ** 10, 1009)):
    long_way = (a * b) % m
    short = (a % m) * (b % m) % m
    print(f"{f'{a} * {b} mod {m}':>34} {long_way:>16} {short:>16} "
          f"{str(long_way == short):>7}")
