"""The sum of the first n integers, proved and then checked."""
from dmkit.induct import check_identity, closed_sum, sum_to

# CLAIM. 1 + 2 + ... + n = n(n+1)/2.
# BASE.  n = 1: the sum is 1 and the formula gives 1(2)/2 = 1.
# STEP.  Assume it holds at n. Then the sum to n+1 is n(n+1)/2 + (n+1), which is
#        (n+1)(n+2)/2 -- the formula at n+1. So it passes from each value to the next.
print(f"{'n':>5} {'sum 1..n':>12} {'n(n+1)/2':>12} {'agree':>7}")
for n in (1, 2, 3, 10, 100, 1000):
    print(f"{n:>5} {sum_to(n):>12} {closed_sum(n):>12} "
          f"{str(sum_to(n) == closed_sum(n)):>7}")
print()
first = check_identity(sum_to, closed_sum, 1, 5000)
print(f"first disagreement in 1..4999: {first}")
