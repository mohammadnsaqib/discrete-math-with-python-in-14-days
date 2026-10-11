"""The value that undoes a multiplication, when there is one."""
from dmkit.crypto import mod_inverse
from dmkit.number import gcd

for m in (7, 8, 12):
    print(f"modulo {m}:")
    print(f"{'a':>6} {'gcd(a, m)':>11} {'inverse':>9} {'a * inverse mod m':>19}")
    for a in range(1, m):
        inverse = mod_inverse(a, m)
        product = "-" if inverse is None else str(a * inverse % m)
        print(f"{a:>6} {gcd(a, m):>11} {str(inverse):>9} {product:>19}")
    print()
bad = [(a, m) for m in range(2, 60) for a in range(1, m)
       if (mod_inverse(a, m) is None) != (gcd(a, m) != 1)]
print(f"pairs where the presence of an inverse did not match the gcd: {len(bad)}")
wrong = [(a, m) for m in range(2, 60) for a in range(1, m)
         if mod_inverse(a, m) is not None and a * mod_inverse(a, m) % m != 1]
print(f"pairs where the inverse did not multiply to 1: {len(wrong)}")
