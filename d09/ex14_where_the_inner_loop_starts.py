"""Two starting points for the inner loop, and the writes each of them costs."""
from dmkit.number import sieve, sieve_crossings

print(f"{'limit':>10} {'starting at 2p':>16} {'starting at p*p':>17} "
      f"{'writes saved':>14} {'share saved':>13}")
for limit in (100, 1000, 10000, 100000, 1000000):
    naive = sieve_crossings(limit, start_at_square=False)
    smart = sieve_crossings(limit, start_at_square=True)
    print(f"{limit:>10} {naive:>16} {smart:>17} {naive - smart:>14} "
          f"{(naive - smart) / naive:>13.4f}")
print()
p, limit = 7, 100
early = [m for m in range(2 * p, p * p, p)]
print(f"the multiples of {p} below {p}*{p}: {early}")
print("each of them has a factor below 7, so each was crossed out already:")
for m in early:
    factor = next(d for d in range(2, m) if m % d == 0)
    print(f"   {m:>3} was crossed out by {factor}")
print()
def sieve_from_2p(limit):
    """The same sieve with the inner loop starting at 2*p, for comparison."""
    from math import isqrt
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for q in range(2, isqrt(limit) + 1):
        if flags[q]:
            for multiple in range(2 * q, limit + 1, q):
                if multiple != q:
                    flags[multiple] = False
    return [n for n, ok in enumerate(flags) if ok]


print(f"the two starting rules find the same primes below 10000: "
      f"{sieve(10000) == sieve_from_2p(10000)}")
