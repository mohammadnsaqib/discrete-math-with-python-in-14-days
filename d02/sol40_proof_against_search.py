"""Problem 2.27: six claims, each with a proof or a counterexample, never neither."""
from dmkit.proof import counterexample, is_even, is_odd, is_prime_slow

# Each entry: the claim, the predicate, the domain, and what settles it -- either the
# one-line argument, or the member that refutes it.
claims = [
    ("the sum of two even numbers is even",
     lambda t: is_even(t[0] + t[1]), [(a, b) for a in range(0, 40, 2)
                                      for b in range(0, 40, 2)],
     "2a + 2b = 2(a+b)"),
    ("the sum of two odd numbers is odd",
     lambda t: is_odd(t[0] + t[1]), [(a, b) for a in range(1, 40, 2)
                                     for b in range(1, 40, 2)],
     None),
    ("the product of two odd numbers is odd",
     lambda t: is_odd(t[0] * t[1]), [(a, b) for a in range(1, 40, 2)
                                     for b in range(1, 40, 2)],
     "(2a+1)(2b+1) = 2(2ab+a+b) + 1"),
    ("every prime above 2 is odd",
     lambda n: not is_prime_slow(n) or n == 2 or is_odd(n), range(2, 200),
     "2 would divide it"),
    ("if a divides b and b divides c then a divides c",
     lambda t: t[1] % t[0] != 0 or t[2] % t[1] != 0 or t[2] % t[0] == 0,
     [(a, b, c) for a in range(1, 13) for b in range(1, 13) for c in range(1, 13)],
     "b = ka and c = mb, so c = (mk)a"),
    ("every number that divides 12 divides 6",
     lambda n: 12 % n != 0 or 6 % n == 0, range(1, 13), None),
]
print(f"{'claim':>46} {'settled by':>34}")
for text, pred, dom, argument in claims:
    w = counterexample(pred, list(dom))
    if w is not None:
        settled = f"the counterexample {w!r}"
    else:
        settled = argument if argument else "NOTHING -- see below"
    print(f"{text:>46} {settled:>34}")
