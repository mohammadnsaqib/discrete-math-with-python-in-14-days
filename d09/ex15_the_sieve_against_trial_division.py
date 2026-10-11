"""Two ways to list the primes below a limit, and what each costs."""
from dmkit.induct import best_of
from dmkit.number import is_prime_trial, sieve

print(f"{'limit':>10} {'sieve':>8} {'trial division':>16} {'agree':>7}")
for limit in (100, 1000, 10000):
    by_sieve = sieve(limit)
    by_trial = [n for n in range(2, limit + 1) if is_prime_trial(n)]
    print(f"{limit:>10} {len(by_sieve):>8} {len(by_trial):>16} "
          f"{str(by_sieve == by_trial):>7}")
print()
print(f"{'limit':>10} {'sieve, seconds':>16} {'trial, seconds':>16} "
      f"{'times slower':>14}")
for limit in (10000, 40000, 160000):
    fast = best_of(lambda l=limit: sieve(l), 3)
    slow = best_of(lambda l=limit: [n for n in range(2, l + 1) if is_prime_trial(n)], 3)
    print(f"{limit:>10} {fast:>16.6f} {slow:>16.6f} {slow / fast:>14.1f}")
