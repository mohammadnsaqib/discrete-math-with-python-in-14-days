"""One member of the domain, and a claim that does not survive it."""
from dmkit.proof import counterexample, is_prime_slow

claims = [
    ("every prime is odd", lambda n: not is_prime_slow(n) or n % 2 == 1,
     range(2, 100)),
    ("n squared is at least n", lambda n: n * n >= n, range(-5, 20)),
    ("every odd number "
     "above 1 is prime", lambda n: n % 2 == 0 or n <= 1 or is_prime_slow(n),
     range(2, 100)),
    ("if n divides 12 "
     "then n divides 6", lambda n: 12 % n != 0 or 6 % n == 0, range(1, 13)),
]
for text, pred, dom in claims:
    w = counterexample(pred, dom)
    if w is None:
        print(f"{text:>36}: no counterexample in the range searched")
    else:
        print(f"{text:>36}: REFUTED by {w}")
