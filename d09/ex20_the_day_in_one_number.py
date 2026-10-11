"""One number taken through every routine the day has built."""
from math import gcd as library_gcd

from sympy import factorint, isprime

from dmkit.number import (divisors, extended_gcd, factorise, from_factors, gcd,
                          is_prime_trial, lcm, prime_count, sieve)

n, m = 5040, 2079

print(f"{'question':>34} {'answer':>34}")
print(f"{'the factorisation of 5040':>34} {str(factorise(n)):>34}")
print(f"{'multiplied back':>34} {from_factors(factorise(n)):>34}")
print(f"{'SymPy agrees':>34} {str(factorise(n) == sorted(factorint(n).items())):>34}")
print(f"{'how many divisors':>34} {len(divisors(n)):>34}")
from_powers = 1
for _, power in factorise(n):
    from_powers *= power + 1
print(f"{'from the powers':>34} {from_powers:>34}")
print(f"{'is 5040 prime':>34} {str(is_prime_trial(n)):>34}")
print(f"{'SymPy agrees':>34} {str(is_prime_trial(n) == isprime(n)):>34}")
print()
print(f"{'the factorisation of 2079':>34} {str(factorise(m)):>34}")
g, x, y = extended_gcd(n, m)
print(f"{'gcd(5040, 2079)':>34} {g:>34}")
print(f"{'the library agrees':>34} {str(g == library_gcd(n, m)):>34}")
print(f"{'x and y with 5040x + 2079y = gcd':>34} {f'{x}, {y}':>34}")
print(f"{'and that combination gives':>34} {n * x + m * y:>34}")
print(f"{'lcm(5040, 2079)':>34} {lcm(n, m):>34}")
print(f"{'gcd times lcm':>34} {g * lcm(n, m):>34}")
print(f"{'5040 times 2079':>34} {n * m:>34}")
print()
primes = sieve(100)
print(f"primes below 100: {len(primes)}, the largest being {primes[-1]}")
print(f"primes below 5040: {prime_count(5040)}")
print(f"the prime factors of 5040 are {[p for p, _ in factorise(n)]}, "
      f"all below 10")
