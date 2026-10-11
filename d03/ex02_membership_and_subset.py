"""Being a member and being a subset are different relations."""
from dmkit.sets import as_text

A = {1, 2, 3}
B = {1, 2}
nested = {frozenset({1, 2}), 3}

print(f"A       = {as_text(A)}")
print(f"B       = {as_text(B)}")
print(f"nested  = a set whose members are the SET {{1, 2}} and the number 3")
print()
print(f"   1 is a member of A            : {1 in A}")
print(f"   B is a subset of A            : {B <= A}")
print(f"   B is a member of A            : {frozenset(B) in A}")
print(f"   B is a member of nested       : {frozenset(B) in nested}")
print(f"   B is a subset of nested       : {B <= nested}")
print()
print("B is inside A in one sense and inside nested in the other, and the two senses")
print("have nothing to do with each other. The empty set is a subset of every set and")
print(f"a member of almost none: empty subset of A is {set() <= A}, member is "
      f"{frozenset() in A}.")
