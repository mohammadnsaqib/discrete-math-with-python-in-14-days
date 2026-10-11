"""Four counting problems that produce a recurrence rather than a formula."""
from dmkit.recur import iterate


def by_hand_binary_no_two_ones(length):
    """Binary strings of the length with no two 1s next to each other, built and
    counted."""
    from itertools import product
    return len([t for t in product("01", repeat=length)
                if all(not (a == b == "1") for a, b in zip(t, t[1:]))])


print(f"{'problem':>34} {'the recurrence':>26} {'first eight terms':>30}")
print(f"{'subsets of n items':>34} {'a(n) = 2*a(n-1)':>26} "
      f"{str(iterate([2], [1], 8)):>30}")
print(f"{'moves for n discs':>34} {'a(n) = 2*a(n-1) + 1':>26} "
      f"{str(iterate([2], [0], 8, lambda n: 1)):>30}")
print(f"{'binary strings, no two 1s':>34} {'a(n) = a(n-1) + a(n-2)':>26} "
      f"{str(iterate([1, 1], [1, 2], 8)):>30}")
print(f"{'arrangements of n items':>34} {'a(n) = n*a(n-1)':>26} "
      f"{str([1, 1, 2, 6, 24, 120, 720, 5040]):>30}")
print()
print(f"{'length':>8} {'by the recurrence':>19} {'by building':>13} {'agree':>7}")
strings = iterate([1, 1], [1, 2], 12)
for length in range(0, 10):
    built = by_hand_binary_no_two_ones(length)
    print(f"{length:>8} {strings[length]:>19} {built:>13} "
          f"{str(strings[length] == built):>7}")
