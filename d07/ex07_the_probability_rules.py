"""Six checks of the rules of probability, each made against the sample space it is
claimed over."""
from fractions import Fraction

from dmkit.prob import probability, sample_space

space = sample_space(range(1, 7), repeat=2)
seven = lambda o: sum(o) == 7
low = lambda o: sum(o) < 5
six = lambda o: 6 in o

checks = [
    ("every probability is in 0..1",
     all(0 <= probability(space, e) <= 1 for e in (seven, low, six))),
    ("the whole space has probability 1",
     probability(space, lambda o: True) == 1),
    ("the empty event has probability 0",
     probability(space, lambda o: False) == 0),
    ("complement: P(not A) is 1 - P(A)",
     probability(space, lambda o: not seven(o)) == 1 - probability(space, seven)),
    ("union of two that never overlap adds",
     probability(space, lambda o: seven(o) or low(o))
     == probability(space, seven) + probability(space, low)),
    ("union in general needs the overlap out",
     probability(space, lambda o: seven(o) or six(o))
     == probability(space, seven) + probability(space, six)
     - probability(space, lambda o: seven(o) and six(o))),
]
print(f"{'rule':>40} {'holds':>7}")
for text, ok in checks:
    print(f"{text:>40} {str(ok):>7}")
print()
print(f"{'P(sum is 7)':>26} {str(probability(space, seven)):>8}")
print(f"{'P(sum below 5)':>26} {str(probability(space, low)):>8}")
print(f"{'P(at least one six)':>26} {str(probability(space, six)):>8}")
print(f"{'P(7 and a six)':>26} "
      f"{str(probability(space, lambda o: seven(o) and six(o))):>8}")
