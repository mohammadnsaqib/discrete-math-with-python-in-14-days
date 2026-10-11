"""The oldest proof in the book, run rather than recited."""
from dmkit.number import factorise, is_prime_trial, sieve


def one_more_prime(known):
    """A prime that is not in the given list, built from the list itself.

    Multiply everything in the list and add 1. The result leaves remainder 1 on division
    by each of them, so none of them divides it, and its own prime factors are therefore
    new. THE PRODUCT PLUS ONE NEED NOT BE PRIME ITSELF, which is the step people
    misremember.
    """
    candidate = 1
    for p in known:
        candidate *= p
    candidate += 1
    return candidate, factorise(candidate)


print(f"{'known primes':>26} {'product + 1':>14} {'prime?':>8} {'its factors':>22}")
known = [2]
for _ in range(6):
    candidate, factors = one_more_prime(known)
    print(f"{str(known):>26} {candidate:>14} {str(is_prime_trial(candidate)):>8} "
          f"{str([p for p, _ in factors]):>22}")
    known = sorted(known + [factors[0][0]])
print()
print(f"the list grew to {known}, all of them prime: "
      f"{all(is_prime_trial(p) for p in known)}")
print()
first = sieve(20)
candidate, factors = one_more_prime(first)
print(f"starting from every prime below 20: {first}")
print(f"   their product plus one is {candidate}")
print(f"   it is prime: {is_prime_trial(candidate)}")
print(f"   its factors are {[p for p, _ in factors]}, none of which is in the list")
