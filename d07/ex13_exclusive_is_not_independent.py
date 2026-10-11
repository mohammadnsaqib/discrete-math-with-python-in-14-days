"""Two words that sound alike and mean opposite things."""
from dmkit.prob import conditional, independent, probability, sample_space

space = sample_space(range(1, 7), repeat=2)
pairs = [
    ("the sum is 7", lambda o: sum(o) == 7, "the sum is 8", lambda o: sum(o) == 8),
    ("both match", lambda o: o[0] == o[1], "the sum is 7", lambda o: sum(o) == 7),
    ("first is even", lambda o: o[0] % 2 == 0, "second is even",
     lambda o: o[1] % 2 == 0),
    ("first is a 1", lambda o: o[0] == 1, "second is a 1", lambda o: o[1] == 1),
]
print(f"{'A':>16} {'B':>16} {'P(A and B)':>12} {'never together':>16} "
      f"{'independent':>13}")
for a_name, a, b_name, b in pairs:
    both = probability(space, lambda o: a(o) and b(o))
    print(f"{a_name:>16} {b_name:>16} {str(both):>12} {str(both == 0):>16} "
          f"{str(independent(space, a, b)):>13}")
print()
seven = lambda o: sum(o) == 7
eight = lambda o: sum(o) == 8
print(f"P(sum is 7) is {probability(space, seven)}")
print(f"P(sum is 7 given the sum is 8) is {conditional(space, seven, eight)}")
