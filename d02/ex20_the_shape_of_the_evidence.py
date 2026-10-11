"""What a search costs, and what it buys, at four sizes."""
from dmkit.proof import check_over, is_prime_slow


def sum_of_two_primes(n):
    """True when the even number n is a sum of two primes."""
    return any(is_prime_slow(p) and is_prime_slow(n - p) for p in range(2, n // 2 + 1))


print(f"{'range':>27} {'members checked':>17} {'counterexamples':>17} {'settled?':>10}")
for limit in (100, 500, 2000, 8000):
    r = check_over(sum_of_two_primes, range(4, limit + 1, 2), f"4 to {limit}")
    print(f"{('the even numbers 4 to ' + str(limit)):>27} {r['checked']:>17} "
          f"{int(r['refuted']):>17} {'no':>10}")
