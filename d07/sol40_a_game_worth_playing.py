"""Problem 7.27: six games priced by expectation, and the fair stake for each."""
from fractions import Fraction

from dmkit.prob import expectation, probability, sample_space

two = sample_space(range(1, 7), repeat=2)
three = sample_space(range(1, 7), repeat=3)

games = [
    ("two dice, win on a 7", two, lambda o: sum(o) == 7, 5),
    ("two dice, win on a double", two, lambda o: o[0] == o[1], 5),
    ("two dice, win on any six", two, lambda o: 6 in o, 2),
    ("three dice, win on a triple", three, lambda o: len(set(o)) == 1, 30),
    ("three dice, win on any six", three, lambda o: 6 in o, 1),
    ("three dice, win on a sum of 10", three, lambda o: sum(o) == 10, 7),
]
print(f"{'game':>32} {'P(win)':>10} {'prize':>7} {'expected gain':>15} "
      f"{'fair prize':>12}")
for text, space, wins, prize in games:
    p = probability(space, wins)
    gain = expectation(space, lambda o, w=wins, z=prize: z - 1 if w(o) else -1)
    print(f"{text:>32} {str(p):>10} {prize:>7} {str(gain):>15} {str(1 / p):>12}")
print()
print(f"{'game':>32} {'stake for a fair game':>24}")
for text, space, wins, prize in games:
    p = probability(space, wins)
    print(f"{text:>32} {str(p * prize):>24}")
