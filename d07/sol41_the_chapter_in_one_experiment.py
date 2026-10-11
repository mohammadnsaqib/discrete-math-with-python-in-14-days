"""Problem 7.28: one experiment, every routine of the day, and a simulation beside it.
"""
from fractions import Fraction

from dmkit.prob import (conditional, expectation, independent, probability,
                        sample_space, simulate, variance)

space = sample_space(range(1, 7), repeat=3)
triple = lambda o: len(set(o)) == 1
any_six = lambda o: 6 in o
high = lambda o: sum(o) >= 14

print(f"the sample space holds {len(space)} outcomes")
print()
print(f"{'quantity':>38} {'value':>12} {'as a decimal':>14}")
rows = [
    ("P(all three match)", probability(space, triple)),
    ("P(at least one six)", probability(space, any_six)),
    ("P(sum is 14 or more)", probability(space, high)),
    ("P(all match | at least one six)", conditional(space, triple, any_six)),
    ("P(at least one six | all match)", conditional(space, any_six, triple)),
    ("P(sum is 14 or more | at least one six)", conditional(space, high, any_six)),
    ("the expected sum", expectation(space, sum)),
    ("the variance of the sum", variance(space, sum)),
]
for text, value in rows:
    print(f"{text:>38} {str(value):>12} {float(value):>14.6f}")
print()
print(f"are 'all match' and 'at least one six' independent? "
      f"{independent(space, triple, any_six)}")
print(f"are 'the first is even' and 'the third is even' independent? "
      f"{independent(space, lambda o: o[0] % 2 == 0, lambda o: o[2] % 2 == 0)}")
print()


def roll_three(rng):
    """One trial: three dice from a seeded source."""
    return (rng.randint(1, 6), rng.randint(1, 6), rng.randint(1, 6))


print(f"{'event':>22} {'exact':>12} {'100000 trials':>15} {'error':>10}")
for name, event in (("all three match", triple), ("at least one six", any_six),
                    ("sum is 14 or more", high)):
    exact = probability(space, event)
    seen = simulate(roll_three, event, 100000, seed=20260910)
    print(f"{name:>22} {float(exact):>12.6f} {float(seen):>15.6f} "
          f"{abs(float(seen) - float(exact)):>10.6f}")
