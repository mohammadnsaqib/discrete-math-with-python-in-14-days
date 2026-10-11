"""Every integer above 1 is a product of primes, in one way and one way only."""
from dmkit.number import factorise, from_factors, is_prime_trial

print(f"{'n':>10} {'factorisation':>28} {'multiplied back':>17} {'agree':>7}")
for n in (2, 12, 97, 360, 1024, 999983, 123456):
    factors = factorise(n)
    shown = " * ".join(f"{p}**{k}" if k > 1 else str(p) for p, k in factors)
    print(f"{n:>10} {shown:>28} {from_factors(factors):>17} "
          f"{str(from_factors(factors) == n):>7}")
print()
bad = [n for n in range(2, 20000) if from_factors(factorise(n)) != n]
print(f"integers from 2 to 19999 that do not multiply back: {len(bad)}")
not_prime = [n for n in range(2, 5000)
             if any(not is_prime_trial(p) for p, _ in factorise(n))]
print(f"integers from 2 to 4999 with a non-prime factor reported: {len(not_prime)}")
print()
def every_prime_multiset(n, floor=2):
    """Every non-decreasing list of primes whose product is n, found by search.

    This is the brute-force check on uniqueness. It builds every way of writing n as a
    product of primes rather than trusting that there is only one.
    """
    if n == 1:
        return [[]]
    out = []
    for p in range(floor, n + 1):
        if n % p == 0 and is_prime_trial(p):
            for rest in every_prime_multiset(n // p, p):
                out.append([p] + rest)
    return out


print(f"{'n':>8} {'ways to write it as a product of primes':>42}")
for n in (12, 30, 64, 360, 1155):
    ways = every_prime_multiset(n)
    print(f"{n:>8} {str(ways):>42}")
print()
many = [n for n in range(2, 400) if len(every_prime_multiset(n)) != 1]
print(f"integers from 2 to 399 with more than one such product: {len(many)}")
