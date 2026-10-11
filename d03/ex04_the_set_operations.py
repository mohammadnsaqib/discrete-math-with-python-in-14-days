"""Union, intersection, difference and symmetric difference on one pair of sets."""
from dmkit.sets import as_text

A = {1, 2, 3, 4, 5, 6}
B = {4, 5, 6, 7, 8}
U = set(range(1, 11))

rows = [
    ("A union B", A | B),
    ("A intersect B", A & B),
    ("A minus B", A - B),
    ("B minus A", B - A),
    ("symmetric difference", A ^ B),
    ("complement of A in U", U - A),
]
print(f"A = {as_text(A)}")
print(f"B = {as_text(B)}")
print(f"U = {as_text(U)}")
print()
for name, value in rows:
    print(f"{name:>22} : {as_text(value):<32} {len(value):>3} members")
print()
print(f"|A| + |B| = {len(A) + len(B)}, and |A union B| = {len(A | B)}.")
print(f"the difference is {len(A) + len(B) - len(A | B)}, which is |A intersect B| = "
      f"{len(A & B)}. Day 5 makes a rule of that.")
