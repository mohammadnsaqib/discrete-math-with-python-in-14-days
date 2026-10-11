"""Arithmetic on remainders, and the one system built on it that everybody uses. Day 10.

Day 9 split the integers into groups by their remainder. Today does arithmetic with the
groups themselves: adding, multiplying, and — where it is possible at all — dividing.

DIVISION IS THE INTERESTING ONE. It is possible modulo m exactly when the number being
divided by shares no factor with m, and the Bezout coefficients of Day 9 are the only
way to find the answer. Everything after Section 10.3 rests on that.

EVERY THEOREM HERE IS CHECKED EXHAUSTIVELY ON SMALL MODULI BEFORE IT IS USED ON A LARGE
ONE. That is the whole discipline of the chapter: a theorem used at 2048 bits and never
tested at 7 is a theorem taken on trust, and Day 2 settled what trust is worth.

Python's own `pow(a, b, m)` is the oracle for modular exponentiation. The book's routine
is written out because the reader has to see the halving; the library is what says it is
right.
"""
from dmkit.number import extended_gcd, factorise, gcd, is_prime_trial


# --8<-- congruent
def congruent(a, b, m):
    """True when a and b leave the same remainder on division by m.

    Written as a difference rather than as two remainders, because that is the
    definition that carries: a and b are congruent when m divides a - b. The two forms
    agree for positive m, and Example 10.1 checks that they do rather than assuming it.
    """
    if m == 0:
        raise ValueError("there is no arithmetic modulo zero")
    return (a - b) % m == 0
# --8<--


# --8<-- residues
def residues(m):
    """The m possible remainders modulo m, in order."""
    return list(range(m))
# --8<--


# --8<-- mod_table
def mod_table(m, operation):
    """The full table of one operation modulo m, as a list of rows.

    The whole table is built rather than sampled, because the interesting rows are the
    ones with a zero in them and those are never the rows anybody samples.
    """
    return [[operation(a, b) % m for b in range(m)] for a in range(m)]
# --8<--


# --8<-- mod_inverse
def mod_inverse(a, m):
    """The value x with a*x congruent to 1 modulo m, or None when there is none.

    An inverse exists exactly when a and m share no factor. The proof is Bezout: if a*x
    + m*y = 1 then a*x is 1 more than a multiple of m, so x is the inverse. If the gcd
    is larger than 1 then every multiple of a is a multiple of that gcd, and 1 is not.
    """
    g, x, _ = extended_gcd(a % m, m)
    if g != 1:
        return None
    return x % m
# --8<--


# --8<-- solve_congruence
def solve_congruence(a, b, m):
    """Every x modulo m with a*x congruent to b, in order, or an empty list.

    THE COUNT OF SOLUTIONS IS THE GCD, when the gcd divides b, and zero otherwise. That
    is not a special case bolted on: it is the same statement as Day 9's condition for
    a*x + m*y = b to have a solution at all.
    """
    g = gcd(a, m)
    if b % g != 0:
        return []
    a2, b2, m2 = a // g, b // g, m // g
    base = (mod_inverse(a2, m2) * b2) % m2
    return [(base + k * m2) % m for k in range(g)]
# --8<--


# --8<-- crt
def crt(remainders, moduli):
    """The value modulo the product satisfying every congruence, when the moduli are
    coprime.

    Built one congruence at a time rather than by a formula, so that the step is
    visible: hold a solution to the first k congruences and step it by the running
    product until it satisfies the next. The moduli MUST be pairwise coprime, and this
    checks rather than assuming.
    """
    for i, m in enumerate(moduli):
        for n in moduli[i + 1:]:
            if gcd(m, n) != 1:
                raise ValueError(f"the moduli {m} and {n} share a factor")
    value, running = remainders[0] % moduli[0], moduli[0]
    for r, m in zip(remainders[1:], moduli[1:]):
        step = mod_inverse(running % m, m)
        value += running * (((r - value) % m) * step % m)
        running *= m
    return value % running, running
# --8<--


# --8<-- totient
def totient(n):
    """How many values from 1 to n share no factor with n.

    Computed from the factorisation rather than by counting, and Example 10.13 runs the
    count beside it. For a prime p the answer is p - 1, and for a product of two
    distinct primes it is (p-1)(q-1), which is the number RSA is built on.
    """
    if n < 1:
        return 0
    result = n
    for prime, _ in factorise(n):
        result = result // prime * (prime - 1)
    return result
# --8<--


# --8<-- totient_by_counting
def totient_by_counting(n):
    """The same count, found by testing every value. Slow, and the check on the fast
    one."""
    return sum(1 for a in range(1, n + 1) if gcd(a, n) == 1)
# --8<--


# --8<-- mod_pow
def mod_pow(base, exponent, modulus):
    """base to the exponent modulo the modulus, by repeated squaring.

    THE POINT IS THAT THE NUMBERS NEVER GROW. Computing the power first and reducing
    afterwards would need a number with millions of digits; reducing at every step keeps
    everything below the square of the modulus. Example 10.15 measures the difference.
    """
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result
# --8<--


# --8<-- rsa_keys
def rsa_keys(p, q, e=None):
    """A public and a private key from two primes.

    The public key is the product and an exponent sharing no factor with the totient.
    The private key is that exponent's inverse modulo the totient, which exists for
    exactly the reason Section 10.3 gave. ANYBODY WHO CAN FACTOR THE PRODUCT CAN COMPUTE
    THE PRIVATE KEY, which is why Problem 9.28 measures how hard factoring is.
    """
    if not (is_prime_trial(p) and is_prime_trial(q)):
        raise ValueError("both keys must be built from primes")
    if p == q:
        raise ValueError("the two primes must differ")
    n = p * q
    phi = (p - 1) * (q - 1)
    if e is None:
        e = next(c for c in range(3, phi, 2) if gcd(c, phi) == 1)
    if gcd(e, phi) != 1:
        raise ValueError("the exponent must share no factor with the totient")
    d = mod_inverse(e, phi)
    return {"public": (n, e), "private": (n, d), "phi": phi, "primes": (p, q)}
# --8<--


# --8<-- rsa_encrypt
def rsa_encrypt(message, public):
    """The message raised to the public exponent, modulo the product."""
    n, e = public
    if not 0 <= message < n:
        raise ValueError("the message must be smaller than the modulus")
    return mod_pow(message, e, n)
# --8<--


# --8<-- rsa_decrypt
def rsa_decrypt(cipher, private):
    """The cipher raised to the private exponent, which returns the message."""
    n, d = private
    return mod_pow(cipher, d, n)
# --8<--


def order_of(a, m):
    """The smallest positive k with a**k congruent to 1 modulo m, or None."""
    if gcd(a, m) != 1:
        return None
    value, k = a % m, 1
    while value != 1:
        value = value * a % m
        k += 1
    return k
