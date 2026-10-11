"""Conditioning shrinks the sample space, and both spaces are printed."""
from dmkit.prob import conditional, probability, sample_space

space = sample_space(range(1, 7), repeat=2)
seven = lambda o: sum(o) == 7
first_is_two = lambda o: o[0] == 2
at_least_one_six = lambda o: 6 in o

reduced = [o for o in space if first_is_two(o)]
print(f"the whole space has {len(space)} outcomes")
print(f"given the first die is a 2, {len(reduced)} remain: {reduced}")
print()
print(f"{'question':>44} {'probability':>13} {'as a decimal':>14}")
rows = [
    ("P(sum is 7)", probability(space, seven)),
    ("P(sum is 7 given the first is a 2)", conditional(space, seven, first_is_two)),
    ("P(sum is 7 given at least one six)",
     conditional(space, seven, at_least_one_six)),
    ("P(at least one six given the sum is 7)",
     conditional(space, at_least_one_six, seven)),
]
for text, p in rows:
    print(f"{text:>44} {str(p):>13} {float(p):>14.6f}")
print()
both = probability(space, lambda o: seven(o) and first_is_two(o))
print(f"P(7 and first is 2) is {both}, P(first is 2) is "
      f"{probability(space, first_is_two)}")
print(f"and their quotient is {both / probability(space, first_is_two)}")
