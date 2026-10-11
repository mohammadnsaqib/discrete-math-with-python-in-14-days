"""Two quantifiers, and the order that changes the meaning."""
from dmkit.proof import exists, for_all

dom = range(1, 11)

# for all x, there exists y : x < y
a = for_all(lambda x: exists(lambda y: x < y, dom) is not None, dom)
# there exists y such that for all x : x < y
b = exists(lambda y: for_all(lambda x: x < y, dom), dom)

print("domain: the integers 1 to 10")
print()
print(f"  for all x, there exists y with x < y : {a}")
print(f"  there exists y, for all x with x < y : {b is not None}")
print()
print("the first says every number has something above it, which fails at 10.")
print("the second says one number is above everything, which fails because that")
print("number would have to be above itself.")
print()
smaller = range(1, 5)
a2 = for_all(lambda x: exists(lambda y: x <= y, smaller) is not None, smaller)
b2 = exists(lambda y: for_all(lambda x: x <= y, smaller), smaller)
print("domain: the integers 1 to 4, with < replaced by <=")
print(f"  for all x, there exists y with x <= y : {a2}")
print(f"  there exists y, for all x with x <= y : {b2 is not None}, and that y is {b2}")
