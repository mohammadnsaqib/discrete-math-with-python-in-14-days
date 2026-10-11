"""The laws of sets, checked on every subset pair of a small universe."""

from dmkit.sets import power_set

U = {1, 2, 3, 4}
subsets = power_set(U)
pairs = [(set(a), set(b)) for a in subsets for b in subsets]
triples = [(set(a), set(b), set(c)) for a in subsets for b in subsets for c in subsets]

laws2 = [
    ("commutative union", lambda a, b: a | b == b | a),
    ("commutative intersection", lambda a, b: a & b == b & a),
    ("absorption", lambda a, b: a | (a & b) == a),
    ("de Morgan, union", lambda a, b: U - (a | b) == (U - a) & (U - b)),
    ("de Morgan, intersection", lambda a, b: U - (a & b) == (U - a) | (U - b)),
    ("difference as intersection", lambda a, b: a - b == a & (U - b)),
]
laws3 = [
    ("associative union", lambda a, b, c: (a | b) | c == a | (b | c)),
    ("distributive over union", lambda a, b, c: a & (b | c) == (a & b) | (a & c)),
    ("distributive "
     "over intersection", lambda a, b, c: a | (b & c) == (a | b) & (a | c)),
]
print(f"universe of {len(U)} members, so {len(subsets)} subsets, "
      f"{len(pairs)} pairs and {len(triples)} triples")
print()
print(f"{'law':>32} {'cases':>8} {'holds':>7}")
for name, law in laws2:
    print(f"{name:>32} {len(pairs):>8} {str(all(law(a, b) for a, b in pairs)):>7}")
for name, law in laws3:
    print(f"{name:>32} {len(triples):>8} "
          f"{str(all(law(a, b, c) for a, b, c in triples)):>7}")
