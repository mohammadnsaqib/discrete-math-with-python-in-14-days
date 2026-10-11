"""Reversing a conditional probability, on a space small enough to print."""
from fractions import Fraction

from dmkit.prob import conditional, probability, sample_space

# TWO URNS. Urn A holds 2 red and 3 blue; urn B holds 4 red and 1 blue. An urn is chosen
# at random and one ball is drawn. The sample space is built so that each outcome is
# equally likely: five draws from each urn, ten outcomes in all.
space = [(urn, colour)
         for urn, contents in (("A", "rrbbb"), ("B", "rrrrb"))
         for colour in contents]
red = lambda o: o[1] == "r"
from_a = lambda o: o[0] == "A"

print(f"the {len(space)} equally likely outcomes: {space}")
print()
print(f"{'quantity':>34} {'value':>10} {'as a decimal':>14}")
rows = [("P(urn A)", probability(space, from_a)),
        ("P(red)", probability(space, red)),
        ("P(red given urn A)", conditional(space, red, from_a)),
        ("P(urn A given red)", conditional(space, from_a, red))]
for text, p in rows:
    print(f"{text:>34} {str(p):>10} {float(p):>14.6f}")
print()
prior = probability(space, from_a)
likelihood = conditional(space, red, from_a)
evidence = probability(space, red)
print(f"by the definition: {prior} times {likelihood} over {evidence} is "
      f"{prior * likelihood / evidence}")
print(f"and the direct count gives {conditional(space, from_a, red)}")
