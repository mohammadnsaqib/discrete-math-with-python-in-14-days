"""The average of a quantity over the sample space, computed exactly."""
from dmkit.prob import expectation, probability, sample_space

one = sample_space(range(1, 7))
two = sample_space(range(1, 7), repeat=2)

print(f"{'quantity':>36} {'expectation':>13} {'as a decimal':>14}")
rows = [
    ("one die", one, lambda o: o[0]),
    ("the sum of two dice", two, lambda o: sum(o)),
    ("the larger of two dice", two, lambda o: max(o)),
    ("the smaller of two dice", two, lambda o: min(o)),
    ("the difference, larger minus smaller", two, lambda o: max(o) - min(o)),
    ("1 if the sum is 7, else 0", two, lambda o: 1 if sum(o) == 7 else 0),
]
for text, space, value in rows:
    e = expectation(space, value)
    print(f"{text:>36} {str(e):>13} {float(e):>14.6f}")
print()
print(f"the expected value of one die is {expectation(one, lambda o: o[0])}, "
      f"which is not a face on the die.")
print(f"the last row equals P(sum is 7): {probability(two, lambda o: sum(o) == 7)}")
print(f"and the larger plus the smaller is "
      f"{expectation(two, lambda o: max(o)) + expectation(two, lambda o: min(o))}, "
      f"the same as the sum.")
