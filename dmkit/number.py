"""Divisibility, the Euclidean algorithm, and the primes. Day 9.

Everything here is about the integers and the one operation they are not closed under.
Addition, subtraction and multiplication always land back on an integer; division does
not, and the whole of number theory grows out of that.

TWO REFERENCES RUN BESIDE EVERY ROUTINE. Trial division is slow and certain, and it is
what the fast routines are checked against at every size where it can still finish.
`math.gcd`, `sympy.isprime` and `sympy.factorint` are the second opinion, written by
somebody else. A routine that agrees with one and disagrees with the other has found
something worth reading about, and Day 9 prints both columns rather than one.

NOTHING HERE USES FLOATING POINT. An integer square root is computed with `math.isqrt`,
which is exact; `int(n ** 0.5)` is not, and it is wrong for the first time at a value
small enough that Example 9.10 prints it.
"""
from math import isqrt


# --8<-- divides
def divides(a, b):
    """True when a divides b exactly, with a of zero handled rather than crashing.

    Zero divides only zero. Every integer divides zero. Both of those follow from the
    definition and both surprise people, so the routine states them rather than raising.
    """
    if a == 0:
        return b == 0
    return b % a == 0
# --8<--


# --8<-- division_algorithm
def division_algorithm(a, b):
    """The unique quotient and remainder with the remainder in 0 <= r < b.

    THE RANGE OF THE REMAINDER IS THE WHOLE CONTENT. Any pair with a = q*b + r would do
    otherwise, and there are infinitely many. Insisting that r lands in one window of
    size b makes the pair unique, and Python's own // and % already agree with that
    convention for positive b -- which Example 9.4 checks rather than assumes.
    """
    if b == 0:
        raise ValueError("there is no division by zero")
    q = a // b
    r = a - q * b
    return q, r
# --8<--


# --8<-- gcd_by_subtraction
def gcd_by_subtraction(a, b):
    """The greatest common divisor, found by repeatedly taking the smaller from the
    larger.

    This is the oldest form of the algorithm and the slowest. It is here because the
    step is visible: the pair shrinks and the set of common divisors never changes,
    which is the whole proof. Example 9.7 counts its steps against the remainder form.
    """
    a, b = abs(a), abs(b)
    steps = 0
    while a and b:
        if a > b:
            a -= b
        else:
            b -= a
        steps += 1
    return a or b, steps
# --8<--


# --8<-- gcd
def gcd(a, b):
    """The greatest common divisor, by the Euclidean algorithm.

    Replacing the pair (a, b) by (b, a mod b) leaves the common divisors alone and
    shrinks the numbers fast. That the answer is the last non-zero value is not obvious
    and is worth the two lines it takes to say: every common divisor of a and b divides
    a mod b, and the reverse.
    """
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a
# --8<--


# --8<-- gcd_steps
def gcd_steps(a, b):
    """Every pair the Euclidean algorithm passes through, so the shrinking can be
    printed."""
    a, b = abs(a), abs(b)
    trail = []
    while b:
        q, r = divmod(a, b)
        trail.append((a, b, q, r))
        a, b = b, r
    return a, trail
# --8<--


# --8<-- extended_gcd
def extended_gcd(a, b):
    """The gcd together with x and y satisfying a*x + b*y = gcd(a, b).

    Every common divisor of a and b divides that combination, so the gcd is the SMALLEST
    positive value a*x + b*y can take. Day 10 needs x for the modular inverse and would
    have no other way to find one.
    """
    old_r, r = abs(a), abs(b)
    old_x, x = 1, 0
    old_y, y = 0, 1
    while r:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_x, x = x, old_x - q * x
        old_y, y = y, old_y - q * y
    sign_a = 1 if a >= 0 else -1
    sign_b = 1 if b >= 0 else -1
    return old_r, old_x * sign_a, old_y * sign_b
# --8<--


# --8<-- lcm
def lcm(a, b):
    """The least common multiple, from the gcd rather than by searching for it."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)
# --8<--


# --8<-- is_prime_trial
def is_prime_trial(n):
    """Primality by trial division up to the integer square root.

    Stopping at the square root is a theorem rather than an optimisation: if n = a*b
    with both factors above the square root then a*b is above n. `isqrt` is used because
    it is exact -- Example 9.10 shows a floating-point square root giving the wrong
    bound.
    """
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for d in range(3, isqrt(n) + 1, 2):
        if n % d == 0:
            return False
    return True
# --8<--


# --8<-- sieve
def sieve(limit):
    """Every prime up to the limit, by crossing out multiples.

    The inner loop starts at p*p rather than at 2*p, because every smaller multiple of p
    has a factor below p and was crossed out already. Example 9.13 counts the crossings
    both ways.
    """
    if limit < 2:
        return []
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for p in range(2, isqrt(limit) + 1):
        if flags[p]:
            for multiple in range(p * p, limit + 1, p):
                flags[multiple] = False
    return [n for n, is_p in enumerate(flags) if is_p]
# --8<--


# --8<-- sieve_crossings
def sieve_crossings(limit, start_at_square=True):
    """How many times the sieve writes to the array, under either starting rule."""
    if limit < 2:
        return 0
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    crossings = 0
    for p in range(2, isqrt(limit) + 1):
        if flags[p]:
            first = p * p if start_at_square else 2 * p
            for multiple in range(first, limit + 1, p):
                flags[multiple] = False
                crossings += 1
    return crossings
# --8<--


# --8<-- factorise
def factorise(n):
    """The prime factors of n with their multiplicities, smallest prime first.

    The order is fixed by the loop rather than by a dictionary's iteration, so two runs
    print the same factorisation. That the factorisation is unique is the fundamental
    theorem, and Example 9.16 checks it against an independent implementation rather
    than asserting it.
    """
    if n < 2:
        return []
    factors = []
    d = 2
    while d * d <= n:
        power = 0
        while n % d == 0:
            n //= d
            power += 1
        if power:
            factors.append((d, power))
        d += 1 if d == 2 else 2
    if n > 1:
        factors.append((n, 1))
    return factors
# --8<--


# --8<-- from_factors
def from_factors(factors):
    """The number a factorisation describes, multiplied back out."""
    value = 1
    for prime, power in factors:
        value *= prime ** power
    return value
# --8<--


# --8<-- prime_count
def prime_count(limit):
    """How many primes there are up to the limit, by sieving and counting."""
    return len(sieve(limit))
# --8<--


def divisors(n):
    """Every positive divisor of n, in increasing order."""
    if n < 1:
        return []
    small = [d for d in range(1, isqrt(n) + 1) if n % d == 0]
    large = [n // d for d in reversed(small) if n // d != d]
    return small + large
