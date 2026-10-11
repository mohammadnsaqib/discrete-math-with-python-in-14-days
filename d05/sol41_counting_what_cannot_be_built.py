"""Problem 5.28: a count checked by enumeration, then carried past what can be built."""
from itertools import product


def no_two_adjacent_equal(alphabet, length):
    """Every string of the length over the alphabet with no letter repeated next to
    itself."""
    return ["".join(t) for t in product(alphabet, repeat=length)
            if all(a != b for a, b in zip(t, t[1:]))]


def by_rule(letters, length):
    """The count without building: any first letter, then any letter but the one before.

    The rule is the product rule with a first factor that differs from the rest, which
    is the shape every restricted count in this chapter has.
    """
    if length == 0:
        return 1
    return letters * (letters - 1) ** (length - 1)


alphabet = list("abcd")
print(f"{'length':>8} {'by the rule':>14} {'by building':>14} {'agree':>8}")
for length in range(0, 9):
    counted = by_rule(len(alphabet), length)
    built = len(no_two_adjacent_equal(alphabet, length))
    print(f"{length:>8} {counted:>14} {built:>14} {str(counted == built):>8}")
print()
print(f"the six shortest of length 3: {no_two_adjacent_equal(alphabet, 3)[:6]}")
print()
for length in (20, 40, 60):
    print(f"length {length:>3}: {by_rule(len(alphabet), length)}")
print()
total_at_60 = len(alphabet) ** 60
share = by_rule(len(alphabet), 60) / total_at_60
print(f"all strings of length 60: {total_at_60}")
print(f"the share with no repeat next to itself: {share:.3e}")
