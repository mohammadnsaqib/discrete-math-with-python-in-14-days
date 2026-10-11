"""The words 'at least one' mean count the complement."""
from dmkit.prob import probability, sample_space

print(f"{'dice':>6} {'outcomes':>10} {'no six':>10} {'at least one six':>18} "
      f"{'as a decimal':>14}")
for dice in range(1, 6):
    space = sample_space(range(1, 7), repeat=dice)
    none = probability(space, lambda o: 6 not in o)
    some = probability(space, lambda o: 6 in o)
    print(f"{dice:>6} {len(space):>10} {str(none):>10} {str(some):>18} "
          f"{float(some):>14.6f}")
print()
space = sample_space(range(1, 7), repeat=4)
by_count = {k: len([o for o in space if o.count(6) == k]) for k in range(5)}
print(f"four dice, by how many sixes appear: {by_count}")
print(f"adding the counts for 1, 2, 3 and 4 sixes: "
      f"{sum(by_count[k] for k in range(1, 5))}")
print(f"and 1296 minus the {by_count[0]} with no six is "
      f"{len(space) - by_count[0]}")
