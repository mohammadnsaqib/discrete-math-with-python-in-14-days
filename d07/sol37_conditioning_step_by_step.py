"""Problem 7.26: what each piece of information does to one probability."""
from dmkit.prob import conditional, probability, sample_space

space = sample_space(range(1, 7), repeat=3)
target = lambda o: len(set(o)) == 3

conditions = [
    ("nothing", lambda o: True),
    ("the first is a 1", lambda o: o[0] == 1),
    ("the first two differ", lambda o: o[0] != o[1]),
    ("the first two match", lambda o: o[0] == o[1]),
    ("no die is a 6", lambda o: 6 not in o),
    ("the sum is 10", lambda o: sum(o) == 10),
    ("the sum is 3", lambda o: sum(o) == 3),
]
print(f"the event: all three dice differ")
print(f"{'given':>24} {'space':>8} {'probability':>13} {'as a decimal':>14} "
      f"{'moved by':>10}")
base = probability(space, target)
for text, given in conditions:
    reduced = [o for o in space if given(o)]
    p = conditional(space, target, given)
    print(f"{text:>24} {len(reduced):>8} {str(p):>13} {float(p):>14.6f} "
          f"{float(p - base):>10.6f}")
print()
print(f"the unconditional probability is {base} = {float(base):.6f}")
print(f"the largest move is to 0, on 'the first two match' and on 'the sum is 3'.")
