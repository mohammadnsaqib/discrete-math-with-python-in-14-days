"""Problem 7.25: one report on any event over any finite sample space."""
from dmkit.prob import conditional, expectation, probability, sample_space


def report(space, name, event):
    """Every number the chapter defines for one event, in one line."""
    p = probability(space, event)
    hits = sum(1 for o in space if event(o))
    return (f"{name:>26} {hits:>8} {len(space):>8} {str(p):>10} {float(p):>12.6f} "
            f"{str(1 - p):>10}")


for dice in (1, 2, 3):
    space = sample_space(range(1, 7), repeat=dice)
    print(f"{dice} dice, {len(space)} outcomes")
    print(f"{'event':>26} {'hits':>8} {'of':>8} {'P':>10} {'as a decimal':>12} "
          f"{'P(not)':>10}")
    print(report(space, "the sum is even", lambda o: sum(o) % 2 == 0))
    print(report(space, "at least one six", lambda o: 6 in o))
    print(report(space, "all dice match", lambda o: len(set(o)) == 1))
    print(report(space, "all dice differ", lambda o: len(set(o)) == len(o)))
    print(report(space, f"the sum is at least {4 * dice}",
                 lambda o, d=dice: sum(o) >= 4 * d))
    print()
space = sample_space(range(1, 7), repeat=2)
print(f"{'P(all match)':>34} {str(probability(space, lambda o: len(set(o)) == 1)):>10}")
print(f"{'P(all match | at least one six)':>34} "
      f"{str(conditional(space, lambda o: len(set(o)) == 1, lambda o: 6 in o)):>10}")
print(f"{'expected sum':>34} {str(expectation(space, sum)):>10}")
