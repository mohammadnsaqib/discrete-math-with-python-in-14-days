"""Expectation adds, whether or not the parts are independent."""
from fractions import Fraction

from dmkit.prob import expectation, independent, sample_space

two = sample_space(range(1, 7), repeat=2)
three = sample_space(range(1, 7), repeat=3)

first = lambda o: o[0]
second = lambda o: o[1]
print(f"{'quantity':>34} {'expectation':>13}")
print(f"{'the first die':>34} {str(expectation(two, first)):>13}")
print(f"{'the second die':>34} {str(expectation(two, second)):>13}")
print(f"{'their sum':>34} {str(expectation(two, lambda o: o[0] + o[1])):>13}")
print(f"{'the two expectations added':>34} "
      f"{str(expectation(two, first) + expectation(two, second)):>13}")
print()
larger = lambda o: max(o)
smaller = lambda o: min(o)
print(f"{'the larger die':>34} {str(expectation(two, larger)):>13}")
print(f"{'the smaller die':>34} {str(expectation(two, smaller)):>13}")
print(f"{'larger plus smaller':>34} "
      f"{str(expectation(two, lambda o: max(o) + min(o))):>13}")
print(f"{'the two expectations added':>34} "
      f"{str(expectation(two, larger) + expectation(two, smaller)):>13}")
print()
pair_independent = independent(two, lambda o: max(o) >= 5, lambda o: min(o) >= 3)
print(f"is 'the larger is at least 5' independent of 'the smaller is at least 3'? "
      f"{pair_independent}")
print()
print(f"{'dice':>6} {'expected sum':>14} {'dice times 7/2':>16} {'agree':>7}")
for dice, space in ((1, sample_space(range(1, 7))), (2, two), (3, three)):
    e = expectation(space, sum)
    print(f"{dice:>6} {str(e):>14} {str(Fraction(7 * dice, 2)):>16} "
          f"{str(e == Fraction(7 * dice, 2)):>7}")
