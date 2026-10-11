"""Problem 2.28: a search ends in one of two states, and only one of them is progress.
"""
from dmkit.proof import check_over, is_prime_slow

trials = [
    ("every integer 2..N is prime", is_prime_slow),
    ("every integer 2..N has a prime factor",
     lambda n: any(is_prime_slow(d) and n % d == 0 for d in range(2, n + 1))),
]
print(f"{'claim':>40} {'N':>7} {'checked':>9} {'state after the search':>26}")
for text, pred in trials:
    for limit in (10, 100, 1000):
        r = check_over(pred, range(2, limit + 1), f"2 to {limit}")
        state = (f"settled FALSE by {r['witness']}" if r["refuted"]
                 else "unchanged")
        print(f"{text:>40} {limit:>7} {r['checked']:>9} {state:>26}")
