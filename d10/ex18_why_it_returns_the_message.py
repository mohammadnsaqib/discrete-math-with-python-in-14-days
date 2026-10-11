"""The reason the two exponents undo each other."""
from dmkit.crypto import mod_pow, rsa_keys, totient
from dmkit.number import gcd

keys = rsa_keys(11, 13, e=7)
n, e = keys["public"]
_, d = keys["private"]
phi = keys["phi"]

print(f"n = {n}, totient = {phi}, e = {e}, d = {d}")
print(f"e * d = {e * d}, which is {e * d // phi} * {phi} + 1")
print()
print(f"{'m':>5} {'m**(e*d) mod n':>16} {'m**phi mod n':>14} {'gcd(m, n)':>11} "
      f"{'returns m':>11}")
for m in (2, 3, 11, 13, 45, 100, 142):
    print(f"{m:>5} {mod_pow(m, e * d, n):>16} {mod_pow(m, phi, n):>14} "
          f"{gcd(m, n):>11} {str(mod_pow(m, e * d, n) == m % n):>11}")
print()
coprime = [m for m in range(1, n) if gcd(m, n) == 1]
print(f"values sharing no factor with {n}: {len(coprime)}, and the totient is {phi}")
print(f"all of them satisfy m**phi = 1: "
      f"{all(mod_pow(m, phi, n) == 1 for m in coprime)}")
print()
print(f"e*d is 1 more than {e * d // phi} times the totient, so m**(e*d) is m times")
print(f"(m**phi) raised to {e * d // phi}, and the bracket is 1 for every coprime m.")
print()
sharing = [m for m in range(1, n) if gcd(m, n) != 1]
print(f"the {len(sharing)} values sharing a factor with n also return: "
      f"{all(mod_pow(m, e * d, n) == m for m in sharing)}")
