"""The counting argument that turned up on six of the fourteen days."""
from dmkit.counting import count_functions
from dmkit.sets import power_set

n = 4
rows = [
    ("subsets of a set of "
     "4", len(power_set(set(range(n)))), "each member is in or out"),
    ("rows of a 4-variable table", 2 ** n, "each variable is True or False"),
    ("binary strings of length 4", count_functions(n, 2), "each place is 0 or 1"),
    ("graphs on 4 vertices", 2 ** (n * (n - 1) // 2),
     "each possible edge is there or not"),
    ("Boolean functions of 2 inputs", 2 ** (2 ** 2), "each of 4 rows is True or False"),
]
print(f"{'collection':>30} {'how many':>10} {'the independent choice':>36}")
for name, count, why in rows:
    print(f"{name:>30} {count:>10} {why:>36}")
print()
print(f"{'day':>6} {'where the same rule appeared':>44}")
for day, where in ((1, "rows of a truth table"), (3, "members of a power set"),
                   (5, "the product rule itself"), (6, "the four counting cases"),
                   (11, "graphs on a set of vertices"),
                   (14, "columns a Boolean function can have")):
    print(f"{day:>6} {where:>44}")
