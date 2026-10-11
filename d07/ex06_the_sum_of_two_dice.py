"""One distribution printed in full, with its total checked."""
from fractions import Fraction

from dmkit.prob import expectation, probability, sample_space

space = sample_space(range(1, 7), repeat=2)
sums = sorted(set(sum(o) for o in space))

print(f"{'sum':>6} {'probability':>13} {'as a decimal':>14} {'a bar':>14}")
total = Fraction(0)
for s in sums:
    p = probability(space, lambda o, t=s: sum(o) == t)
    total += p
    print(f"{s:>6} {str(p):>13} {float(p):>14.6f} "
          f"{'*' * (p.numerator * 36 // p.denominator):>14}")
print()
print(f"the probabilities add to {total}")
print(f"the expected sum is {expectation(space, sum)} = "
      f"{float(expectation(space, sum)):.6f}")
print(f"and the expected value of one die is "
      f"{expectation(sample_space(range(1, 7)), lambda o: o[0])}")
