"""Forty-one confirmations, and then a counterexample."""
from dmkit.proof import check_over, is_prime_slow, report


def euler(n):
    """n squared minus n plus 41, which is prime for a surprisingly long time."""
    return n * n - n + 41


print(f"{'n':>4} {'n^2 - n + 41':>14} {'prime?':>8}")
for n in list(range(0, 6)) + [39, 40, 41, 42]:
    print(f"{n:>4} {euler(n):>14} {str(is_prime_slow(euler(n))):>8}")
print()
for limit in (10, 20, 40, 41, 45):
    print(f"  over 0..{limit - 1:<3} " + report(
        check_over(lambda n: is_prime_slow(euler(n)), range(limit),
                   f"the integers 0 to {limit - 1}")))
print()
print(f"at n = 41 the value is {euler(41)}, which is 41 times 41.")
print("The claim held for every n from 0 to 40, which is 41 confirmations,")
print("and failed at the next.")
