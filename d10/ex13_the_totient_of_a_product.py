"""The totient of a product of two distinct primes, which RSA is built on."""
from dmkit.crypto import totient, totient_by_counting
from dmkit.number import gcd, is_prime_trial

print(f"{'p':>5} {'q':>5} {'p*q':>7} {'totient':>9} {'(p-1)(q-1)':>12} {'agree':>7}")
for p, q in ((3, 5), (5, 7), (7, 11), (11, 13), (13, 17), (61, 53)):
    n = p * q
    print(f"{p:>5} {q:>5} {n:>7} {totient(n):>9} {(p - 1) * (q - 1):>12} "
          f"{str(totient(n) == (p - 1) * (q - 1)):>7}")
print()
n = 35
coprime = [a for a in range(1, n) if gcd(a, n) == 1]
sharing = [a for a in range(1, n) if gcd(a, n) != 1]
print(f"modulo {n}: {len(coprime)} values share no factor with it")
print(f"   they are      : {coprime}")
print(f"   the others are: {sharing}")
print(f"   the others are the multiples of 5 and of 7, and there are "
      f"{len(sharing)} of them")
print()
bad = [(p, q) for p in range(2, 40) for q in range(2, 40)
       if is_prime_trial(p) and is_prime_trial(q) and p != q
       and totient(p * q) != (p - 1) * (q - 1)]
print(f"pairs of distinct primes below 40 where the rule fails: {len(bad)}")
