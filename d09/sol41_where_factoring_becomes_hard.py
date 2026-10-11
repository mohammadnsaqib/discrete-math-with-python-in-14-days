"""Problem 9.28: how the cost of factoring depends on the size of the smallest factor.
"""
from dmkit.induct import best_of
from dmkit.number import factorise, from_factors, sieve

primes = sieve(200000)
print(f"{'n':>18} {'its factors':>34} {'multiplies back':>17}")
cases = [(2 ** 40, "a power of two"),
         (3 * 10 ** 12, "a small factor and a large one"),
         (999983 * 2, "twice a large prime"),
         (999983 * 999979, "two large primes")]
for n, _ in cases:
    factors = factorise(n)
    shown = " * ".join(f"{p}**{k}" if k > 1 else str(p) for p, k in factors)
    print(f"{n:>18} {shown:>34} {str(from_factors(factors) == n):>17}")
print()
print(f"{'smallest prime factor':>22} {'n':>18} {'seconds':>12} "
      f"{'candidates tried':>18}")
for index in (10, 100, 1000, 5000, 15000):
    p = primes[index]
    q = primes[index + 1]
    n = p * q
    seconds = best_of(lambda v=n: factorise(v), 3)
    tried = 1 + len(range(3, p + 1, 2))
    print(f"{p:>22} {n:>18} {seconds:>12.6f} {tried:>18}")
