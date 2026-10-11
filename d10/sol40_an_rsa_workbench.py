"""Problem 10.27: every message through every small key pair."""
from dmkit.crypto import rsa_decrypt, rsa_encrypt, rsa_keys
from dmkit.number import gcd, sieve

primes = [p for p in sieve(60) if p > 2]
print(f"{'p':>5} {'q':>5} {'n':>7} {'totient':>9} {'e':>5} {'d':>7} "
      f"{'messages':>10} {'all return':>12} {'fixed points':>14}")
failures = 0
for i, p in enumerate(primes[:6]):
    for q in primes[i + 1:i + 3]:
        keys = rsa_keys(p, q)
        n, e = keys["public"]
        _, d = keys["private"]
        returned = [m for m in range(n)
                    if rsa_decrypt(rsa_encrypt(m, keys["public"]),
                                   keys["private"]) == m]
        fixed = [m for m in range(n) if rsa_encrypt(m, keys["public"]) == m]
        if len(returned) != n:
            failures += 1
        print(f"{p:>5} {q:>5} {n:>7} {keys['phi']:>9} {e:>5} {d:>7} {n:>10} "
              f"{str(len(returned) == n):>12} {len(fixed):>14}")
print()
print(f"key pairs where some message did not return: {failures}")
print()
keys = rsa_keys(11, 13, e=7)
n = keys["public"][0]
print(f"with p = 11, q = 13, e = 7, n = {n}:")
fixed = [m for m in range(n) if rsa_encrypt(m, keys["public"]) == m]
print(f"   messages encrypting to themselves: {len(fixed)}")
print(f"   the first ten: {fixed[:10]}")
print(f"   0, 1 and n-1 are among them: {0 in fixed and 1 in fixed and n - 1 in fixed}")
print()
bad_e = [e for e in range(2, keys["phi"]) if gcd(e, keys["phi"]) != 1]
print(f"exponents below the totient that cannot be used: {len(bad_e)}")
print(f"   the smallest few: {bad_e[:8]}")
