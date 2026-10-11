"""How the primes are spread, counted rather than described."""
from dmkit.number import prime_count, sieve

primes = sieve(1000)
print(f"the primes below 100: {[p for p in primes if p < 100]}")
print()
print(f"{'range':>18} {'primes in it':>14} {'share':>8}")
for start in range(0, 1000, 100):
    inside = [p for p in primes if start <= p < start + 100]
    print(f"{f'{start} to {start + 99}':>18} {len(inside):>14} "
          f"{len(inside) / 100:>8.2f}")
print()
print(f"{'limit':>10} {'primes up to it':>17} {'share':>8}")
for limit in (10, 100, 1000, 10000, 100000):
    count = prime_count(limit)
    print(f"{limit:>10} {count:>17} {count / limit:>8.4f}")
print()
gaps = [(primes[i + 1] - primes[i], primes[i]) for i in range(len(primes) - 1)]
biggest = max(gaps)
print(f"the largest gap between primes below 1000 is {biggest[0]}, after {biggest[1]}")
runs = [(a, b) for a, b in zip(primes, primes[1:]) if b - a == 2]
print(f"pairs two apart below 1000: {len(runs)}, the last being {runs[-1]}")
