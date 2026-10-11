"""A relation is nothing more than a set of ordered pairs."""
from dmkit.sets import as_text, cartesian

people = {"ann", "bob", "cal"}
knows = {("ann", "bob"), ("bob", "ann"), ("bob", "cal"), ("ann", "ann")}

print(f"the domain      : {as_text(people)}")
print(f"every possible pair: {len(cartesian(people, people))}")
print(f"the relation has: {len(knows)} of them")
print()
print(f"{'pair':>14} {'in the relation?':>18}")
for pair in cartesian(people, people):
    print(f"{str(pair):>14} {str(pair in knows):>18}")
print()
print("a relation is a subset of the square, so there are 2 to the power 9 relations")
print(f"on three people: {2 ** 9}. Choosing one is choosing which of the nine pairs to")
print("include, which is Day 1's choice again.")
