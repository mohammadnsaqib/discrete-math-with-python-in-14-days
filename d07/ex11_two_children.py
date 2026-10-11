"""One question, two readings, and two different correct answers."""
from dmkit.prob import conditional, probability, sample_space

space = sample_space("BG", repeat=2)
print(f"the four families: {[''.join(o) for o in space]}")
print()
at_least_one_boy = lambda o: "B" in o
both_boys = lambda o: o == ("B", "B")
older_is_boy = lambda o: o[0] == "B"

rows = [
    ("P(both boys)", probability(space, both_boys),
     [o for o in space if both_boys(o)]),
    ("P(both boys given at least one boy)",
     conditional(space, both_boys, at_least_one_boy),
     [o for o in space if at_least_one_boy(o)]),
    ("P(both boys given the older is a boy)",
     conditional(space, both_boys, older_is_boy),
     [o for o in space if older_is_boy(o)]),
]
print(f"{'question':>40} {'probability':>13} {'space it is over':>26}")
for text, p, reduced in rows:
    print(f"{text:>40} {str(p):>13} {str([''.join(o) for o in reduced]):>26}")
