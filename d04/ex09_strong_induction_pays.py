"""Two claims that ordinary induction cannot reach and strong induction can."""
from dmkit.induct import fib_iterative
from dmkit.proof import is_prime_slow

# CLAIM ONE. Every integer above 1 is a product of primes. CLAIM TWO. Every amount of 8
# or more can be paid in 3s and 5s. Both steps reach back further than one value: the
# first to two factors, the second to n-3.


def as_primes(n):
    """The prime factors of n, smallest first, by repeated division."""
    factors, d = [], 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors


def payable(n):
    """True when n can be made from 3s and 5s."""
    return any(3 * a + 5 * b == n for a in range(n // 3 + 1) for b in range(n // 5 + 1))


print(f"{'n':>5} {'as a product of primes':>26}")
for n in (12, 17, 60, 97, 360):
    print(f"{n:>5} {str(as_primes(n)):>26}")
print()
cannot = [n for n in range(1, 40) if not payable(n)]
print(f"amounts below 40 that cannot be paid in 3s and 5s: {cannot}")
print(f"the largest of them is {max(cannot)}, so the base cases are 8, 9 and 10.")
