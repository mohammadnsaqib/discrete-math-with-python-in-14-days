"""Problem 9.25: everything the chapter can say about one integer, in one report."""
from sympy import factorint, isprime

from dmkit.number import divisors, factorise, from_factors, is_prime_trial


def report(n):
    """One line of facts about n, each of them computed rather than looked up."""
    factors = factorise(n)
    count = 1
    for _, power in factors:
        count *= power + 1
    shown = " * ".join(f"{p}**{k}" if k > 1 else str(p) for p, k in factors)
    return {"n": n, "prime": is_prime_trial(n), "factors": shown,
            "divisors": len(divisors(n)), "from_powers": count,
            "sum": sum(divisors(n)),
            "checks": (
                from_factors(factors) == n
                and is_prime_trial(n) == isprime(n)
                and factors == sorted(factorint(n).items())
                and len(divisors(n)) == count)}


print(f"{'n':>8} {'prime':>7} {'factorisation':>24} {'divisors':>9} {'their sum':>11} "
      f"{'all checks pass':>16}")
for n in (2, 12, 28, 97, 360, 496, 1024, 5040, 8128, 999983):
    r = report(n)
    print(f"{r['n']:>8} {str(r['prime']):>7} {r['factors']:>24} {r['divisors']:>9} "
          f"{r['sum']:>11} {str(r['checks']):>16}")
print()
failed = [n for n in range(2, 5000) if not report(n)["checks"]]
print(f"integers from 2 to 4999 where any check failed: {len(failed)}")
print()
perfect = [n for n in range(2, 10000) if sum(divisors(n)) == 2 * n]
print(f"integers below 10000 whose divisors add to twice themselves: {perfect}")
