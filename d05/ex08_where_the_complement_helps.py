"""How much work the complement saves, counted in cases rather than in seconds."""
from dmkit.counting import complement_rule, count_functions, strings_over

alphabet = list("abc")
print(f"{'length':>8} {'total':>10} {'no a':>10} {'at least one a':>16} "
      f"{'direct cases':>14}")
for length in range(1, 9):
    total = count_functions(length, len(alphabet))
    none = count_functions(length, len(alphabet) - 1)
    print(f"{length:>8} {total:>10} {none:>10} "
          f"{complement_rule(total, none):>16} {length:>14}")
print()
built = [s for s in strings_over(alphabet, 5) if "a" in s]
print(f"the count at length 5, by building: {len(built)}")
print(f"the first four of them: {built[:4]}")
