"""A predicate has no truth value until its variable is given one."""
from dmkit.proof import divides, is_even, is_prime_slow


def bigger_than_five(n):
    """The predicate 'n is greater than five'."""
    return n > 5


print("the predicate 'n > 5' has no value on its own. Give it one:")
for n in (3, 5, 6, 100):
    print(f"   n = {n:>4}: {bigger_than_five(n)}")
print()
print(f"{'n':>5} {'n > 5':>7} {'n is even':>11} {'n is prime':>12} {'3 divides n':>13}")
for n in (2, 3, 6, 7, 9, 12):
    print(f"{n:>5} {str(bigger_than_five(n)):>7} {str(is_even(n)):>11} "
          f"{str(is_prime_slow(n)):>12} {str(divides(3, n)):>13}")
