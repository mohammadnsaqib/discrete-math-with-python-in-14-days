"""An event is a question about an outcome, not a list of outcomes."""
from dmkit.prob import probability, sample_space

space = sample_space(range(1, 7), repeat=2)

events = [
    ("the sum is 7", lambda o: sum(o) == 7),
    ("both dice match", lambda o: o[0] == o[1]),
    ("at least one six", lambda o: 6 in o),
    ("the sum is even", lambda o: sum(o) % 2 == 0),
    ("the first is larger", lambda o: o[0] > o[1]),
    ("the sum is 13", lambda o: sum(o) == 13),
]
print(f"{'event':>22} {'outcomes':>10} {'of':>5} {'probability':>13} "
      f"{'as a decimal':>14}")
for text, event in events:
    hits = [o for o in space if event(o)]
    p = probability(space, event)
    print(f"{text:>22} {len(hits):>10} {len(space):>5} {str(p):>13} {float(p):>14.6f}")
print()
print(f"the outcomes summing to 7: {[o for o in space if sum(o) == 7]}")
