"""Independence checked as an equation on three probabilities."""
from dmkit.prob import conditional, independent, probability, sample_space

space = sample_space(range(1, 7), repeat=2)
pairs = [
    ("first is "
     "even", lambda o: o[0] % 2 == 0, "second is even", lambda o: o[1] % 2 == 0),
    ("first is even", lambda o: o[0] % 2 == 0, "the sum is 7", lambda o: sum(o) == 7),
    ("first is a 6", lambda o: o[0] == 6, "the sum is 7", lambda o: sum(o) == 7),
    ("the sum is 7", lambda o: sum(o) == 7, "both match", lambda o: o[0] == o[1]),
    ("the sum is even", lambda o: sum(o) % 2 == 0, "first is even",
     lambda o: o[0] % 2 == 0),
]
print(f"{'A':>18} {'B':>18} {'P(A)':>7} {'P(B)':>7} {'P(A and B)':>12} "
      f"{'P(A)P(B)':>10} {'independent':>13}")
for first_name, first, second_name, second in pairs:
    pa = probability(space, first)
    pb = probability(space, second)
    both = probability(space, lambda o: first(o) and second(o))
    print(f"{first_name:>18} {second_name:>18} {str(pa):>7} {str(pb):>7} "
          f"{str(both):>12} {str(pa * pb):>10} "
          f"{str(independent(space, first, second)):>13}")
