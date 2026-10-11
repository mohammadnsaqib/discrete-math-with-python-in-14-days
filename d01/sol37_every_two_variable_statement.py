"""Problem 1.26: how many statements of two variables there are, by building all of
them."""
from itertools import product

from dmkit.logic import assignments

names = ["p", "q"]
rows = list(assignments(names))
print(f"assignments of {len(names)} variables: {len(rows)}")

# A statement of two variables IS its column: four entries, each True or False. So there
# are exactly 2**4 of them, and they can all be built.
columns = list(product([False, True], repeat=len(rows)))
print(f"possible columns, and so possible statements: {len(columns)}")
print()
named = {
    (False, False, False, False): "contradiction",
    (False, False, False, True): "p and q",
    (False, True, True, True): "p or q",
    (True, True, False, True): "p implies q",
    (True, False, False, True): "p iff q",
    (True, True, True, True): "tautology",
    (False, True, True, False): "p xor q",
    (True, True, True, False): "not (p and q)",
}
print(f"{'column':>28} {'name':>16}")
for col in columns:
    label = named.get(col, "")
    if label:
        print(f"{str([str(c)[0] for c in col]):>28} {label:>16}")
print()
print(f"{len(named)} of the {len(columns)} have ordinary names. The rest are no less "
      f"real")
print("and nobody has bothered to name them, because each is a combination of these.")
