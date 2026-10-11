"""Three claims proved on paper, and the same three put through a finite check."""
from dmkit.proof import check_over, divides, is_even, is_odd, report

# Each claim below has a two-line proof. The searches do not replace them; they are what
# would have caught a mistake in one.
claims = [
    # the sum of two odd numbers is even: (2a+1) + (2b+1) = 2(a+b+1)
    ("the sum of any two odd numbers below 60 is even",
     lambda pair: is_even(pair[0] + pair[1]),
     [(a, b) for a in range(1, 60, 2) for b in range(1, 60, 2)],
     "the pairs of odd numbers below 60"),
    # the square of an even number is divisible by 4: (2a)^2 = 4a^2
    ("the square of any even number below 100 is divisible by 4",
     lambda n: divides(4, n * n), list(range(0, 100, 2)),
     "the even numbers below 100"),
    # n(n+1) is even, because one of two consecutive integers is even
    ("n times n+1 is even for every n from 1 to 500",
     lambda n: is_even(n * (n + 1)), list(range(1, 501)),
     "the integers 1 to 500"),
]
for text, pred, dom, desc in claims:
    print(text)
    print("   " + report(check_over(pred, dom, desc)))
