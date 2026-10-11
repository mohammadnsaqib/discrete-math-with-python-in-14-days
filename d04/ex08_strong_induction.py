"""Assuming the claim for every smaller value, not only the one before."""
from dmkit.induct import check_identity
from dmkit.proof import is_prime_slow

# CLAIM. Every integer above 1 has a prime factor. ORDINARY INDUCTION cannot reach this:
# knowing n has a prime factor says nothing about n+1. STRONG INDUCTION does: if n is
# prime it is its own prime factor. If not, n = ab with both below n, and the assumption
# covers a -- so a has a prime factor, and it divides n.


def has_prime_factor(n):
    """True when some prime divides n."""
    return any(is_prime_slow(d) and n % d == 0 for d in range(2, n + 1))


print(f"{'n':>5} {'prime?':>8} {'a prime factor':>16} {'from which value':>18}")
for n in (2, 3, 4, 12, 17, 91, 97, 100):
    factor = next(d for d in range(2, n + 1) if is_prime_slow(d) and n % d == 0)
    source = "itself" if is_prime_slow(n) else f"a factor below {n}"
    print(f"{n:>5} {str(is_prime_slow(n)):>8} {factor:>16} {source:>18}")
print()
bad = [n for n in range(2, 2000) if not has_prime_factor(n)]
print(f"integers from 2 to 1999 with no prime factor: {bad}")
