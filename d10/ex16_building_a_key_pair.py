"""A key pair from two primes, with every step checked as it is taken."""
from dmkit.crypto import mod_inverse, rsa_keys, totient
from dmkit.number import gcd

p, q = 61, 53
keys = rsa_keys(p, q, e=17)
n, e = keys["public"]
_, d = keys["private"]
phi = keys["phi"]

print(f"the two primes        : {p} and {q}")
print(f"their product         : {n}")
print(f"the totient           : {phi}, which is ({p} - 1) * ({q} - 1)")
print(f"and totient() agrees  : {totient(n) == phi}")
print(f"the public exponent   : {e}, and gcd({e}, {phi}) is {gcd(e, phi)}")
print(f"the private exponent  : {d}")
print(f"check                 : {e} * {d} = {e * d}, "
      f"which is {e * d // phi} * {phi} + {e * d % phi}")
print(f"and mod_inverse agrees: {mod_inverse(e, phi) == d}")
print()
print(f"{'p':>6} {'q':>6} {'n':>10} {'totient':>10} {'e':>6} {'d':>10} "
      f"{'e*d mod totient':>17}")
for p, q in ((3, 11), (5, 11), (11, 13), (17, 19), (61, 53), (101, 103)):
    keys = rsa_keys(p, q)
    n, e = keys["public"]
    _, d = keys["private"]
    phi = keys["phi"]
    print(f"{p:>6} {q:>6} {n:>10} {phi:>10} {e:>6} {d:>10} {e * d % phi:>17}")
