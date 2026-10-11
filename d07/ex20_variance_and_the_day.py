"""Spread measured two ways, and the day's machinery used once more."""
from fractions import Fraction

from dmkit.prob import expectation, sample_space, variance

one = sample_space(range(1, 7))
two = sample_space(range(1, 7), repeat=2)


def variance_the_other_way(space, value):
    """The mean of the squares minus the square of the mean."""
    return (expectation(space, lambda o: Fraction(value(o)) ** 2)
            - expectation(space, value) ** 2)


print(f"{'quantity':>22} {'mean':>10} {'variance':>14} {'the other route':>17} "
      f"{'agree':>7}")
rows = [("one die", one, lambda o: o[0]),
        ("the sum of two", two, lambda o: sum(o)),
        ("the larger of two", two, lambda o: max(o)),
        ("1 if the sum is 7", two, lambda o: 1 if sum(o) == 7 else 0)]
for text, space, value in rows:
    v = variance(space, value)
    other = variance_the_other_way(space, value)
    print(f"{text:>22} {str(expectation(space, value)):>10} {str(v):>14} "
          f"{str(other):>17} {str(v == other):>7}")
print()
one_die = variance(one, lambda o: o[0])
sum_two = variance(two, lambda o: sum(o))
print(f"the variance of one die is {one_die} and of the sum of two is {sum_two}")
print(f"twice the first is {2 * one_die}, and they agree: {2 * one_die == sum_two}")
print()
larger = variance(two, lambda o: max(o))
smaller = variance(two, lambda o: min(o))
combined = variance(two, lambda o: max(o) + min(o))
print(f"the variance of the larger is {larger} and of the smaller is {smaller}")
print(f"added, that is {larger + smaller}")
print(f"the variance of larger plus smaller is {combined}")
print(f"they agree: {larger + smaller == combined}")
