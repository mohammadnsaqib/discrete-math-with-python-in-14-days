"""The existential quantifier, and the witness that settles it."""
from dmkit.proof import divides, exists, is_even, is_prime_slow

claims = [
    ("an even prime", lambda n: is_prime_slow(n) and is_even(n), range(2, 60)),
    ("a prime above 50", lambda n: is_prime_slow(n) and n > 50, range(2, 60)),
    ("a number below 60 divisible by 7 and by 9",
     lambda n: divides(7, n) and divides(9, n), range(1, 60)),
    ("a perfect square that is also a cube, above 1",
     lambda n: round(n ** 0.5) ** 2 == n and round(n ** (1 / 3)) ** 3 == n,
     range(2, 100)),
]
for text, pred, dom in claims:
    found = exists(pred, dom)
    verdict = (f"yes, witnessed by {found}" if found is not None
               else "none in this range")
    print(f"{text:>50}: {verdict}")
