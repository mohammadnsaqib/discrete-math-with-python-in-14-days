"""For a prime modulus, every non-zero value raised to one less than it gives 1."""
from dmkit.number import gcd, is_prime_trial

for p in (5, 7, 11):
    print(f"modulo {p}: a**{p - 1} for a = 1 to {p - 1}")
    print(f"   {[pow(a, p - 1, p) for a in range(1, p)]}")
print()
print(f"{'m':>5} {'prime':>7} {'values a with a**(m-1) = 1':>28} {'holds for all':>15}")
for m in range(3, 20):
    working = [a for a in range(1, m) if pow(a, m - 1, m) == 1]
    print(f"{m:>5} {str(is_prime_trial(m)):>7} {len(working):>28} "
          f"{str(len(working) == m - 1):>15}")
print()
failures = [m for m in range(3, 2000)
            if is_prime_trial(m) and any(pow(a, m - 1, m) != 1 for a in range(1, m))]
print(f"primes below 2000 where the theorem fails: {failures}")
liars = [m for m in range(3, 2000)
         if not is_prime_trial(m)
         and all(pow(a, m - 1, m) == 1 for a in range(1, m) if gcd(a, m) == 1)]
print(f"composites below 2000 that pass for every value coprime to them: {liars}")
for m in liars:
    factor = next(d for d in range(2, m) if m % d == 0)
    print(f"   {m} = {factor} * {m // factor}")
