"""A counterexample is usually small, and usually at an edge."""
from dmkit.proof import counterexample, is_prime_slow

claims = [
    ("n squared is greater than n", lambda n: n * n > n, range(-3, 30)),
    ("the sum of two primes is even",
     lambda pair: (pair[0] + pair[1]) % 2 == 0,
     [(a, b) for a in range(2, 30) if is_prime_slow(a)
      for b in range(2, 30) if is_prime_slow(b)]),
    ("some two of any three integers sum to an even number",
     lambda t: any((t[i] + t[j]) % 2 == 0 for i in range(3) for j in range(i + 1, 3)),
     [(a, b, c) for a in range(4) for b in range(4) for c in range(4)]),
    ("n cubed is bigger than n squared", lambda n: n ** 3 > n ** 2, range(-2, 20)),
]
for text, pred, dom in claims:
    dom = list(dom)
    w = counterexample(pred, dom)
    where = dom.index(w) + 1 if w is not None else None
    if w is None:
        print(f"{text:>48}: none in {len(dom)} members")
    else:
        print(f"{text:>48}: REFUTED by {w!r}, member {where} of {len(dom)}")
