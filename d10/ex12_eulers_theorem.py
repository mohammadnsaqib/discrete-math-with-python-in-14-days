"""The same statement for any modulus, with the right exponent."""
from dmkit.crypto import totient, totient_by_counting
from dmkit.number import gcd, is_prime_trial

print(f"{'n':>5} {'totient':>9} {'by counting':>13} {'agree':>7} {'n - 1':>7} "
      f"{'prime':>7}")
for n in (5, 7, 8, 9, 12, 15, 16, 35, 97):
    print(f"{n:>5} {totient(n):>9} {totient_by_counting(n):>13} "
          f"{str(totient(n) == totient_by_counting(n)):>7} {n - 1:>7} "
          f"{str(is_prime_trial(n)):>7}")
print()
bad = [n for n in range(1, 500) if totient(n) != totient_by_counting(n)]
print(f"values below 500 where the two totients differ: {len(bad)}")
print()
print(f"{'n':>5} {'totient':>9} {'a**totient = 1 for every coprime a':>36}")
for n in (8, 9, 12, 15, 16, 35):
    coprime = [a for a in range(1, n) if gcd(a, n) == 1]
    ok = all(pow(a, totient(n), n) == 1 for a in coprime)
    print(f"{n:>5} {totient(n):>9} {str(ok):>36}")
print()
print()
n = 35
print(f"modulo {n}, the totient is {totient(n)} and n - 1 is {n - 1}")
for a in (2, 3, 4, 6):
    print(f"   {a}**{totient(n)} = {pow(a, totient(n), n)}, "
          f"{a}**{n - 1} = {pow(a, n - 1, n)}")
print()
failures = [n for n in range(2, 600)
            if any(pow(a, totient(n), n) != 1 for a in range(1, n) if gcd(a, n) == 1)]
print(f"moduli below 600 where the theorem fails: {failures}")
