"""A relation that orders some pairs and leaves others incomparable."""
from dmkit.sets import (is_antisymmetric, is_reflexive, is_symmetric,
                        is_transitive)

dom = {1, 2, 3, 4, 6, 12}
divides = {(a, b) for a in dom for b in dom if b % a == 0}

print("relation: a divides b, on the divisors of 12")
print(f"   reflexive     : {is_reflexive(divides, dom)}")
print(f"   antisymmetric : {is_antisymmetric(divides)}")
print(f"   transitive    : {is_transitive(divides)}")
print(f"   symmetric     : {is_symmetric(divides)}")
print()
incomparable = sorted((a, b) for a in sorted(dom) for b in sorted(dom)
                      if a < b and (a, b) not in divides and (b, a) not in divides)
print(f"pairs where neither divides the other: {incomparable}")
print()
print(f"of the {len(dom) * (len(dom) - 1) // 2} unordered pairs, "
      f"{len(incomparable)} are incomparable.")
