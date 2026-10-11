"""The universal quantifier, and the single member that decides against it."""
from dmkit.proof import counterexample, for_all, is_prime_slow

claims = [
    ("every integer 2 to 20 has a prime factor",
     lambda n: any(is_prime_slow(d) and n % d == 0 for d in range(2, n + 1)),
     range(2, 21)),
    ("every integer 2 to 20 is prime", is_prime_slow, range(2, 21)),
    ("every square below 100 is non-negative", lambda n: n * n >= 0, range(-9, 10)),
    ("every integer 1 to 30 that ends in 5 is divisible by 5",
     lambda n: n % 10 != 5 or n % 5 == 0, range(1, 31)),
]
for text, pred, dom in claims:
    holds = for_all(pred, dom)
    print(f"{str(holds):>6}  {text}")
    if not holds:
        print(f"        first member where it fails: {counterexample(pred, dom)}")
