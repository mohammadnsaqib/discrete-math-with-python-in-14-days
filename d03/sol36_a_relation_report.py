"""Problem 3.25: one report on any relation, naming what it is."""
from dmkit.sets import (equivalence_classes, is_antisymmetric, is_reflexive,
                        is_symmetric, is_transitive)


def describe(name, relation, domain):
    """Every property, and the name the combination earns."""
    r = is_reflexive(relation, domain)
    s = is_symmetric(relation)
    t = is_transitive(relation)
    a = is_antisymmetric(relation)
    if r and s and t:
        kind = "an equivalence relation"
    elif r and a and t:
        kind = "a partial order"
    else:
        kind = "none of the named kinds"
    print(f"{name:>26} {str(r):>7} {str(s):>7} {str(t):>7} {str(a):>7}  {kind}")
    if r and s and t:
        print(f"{'':>26} classes: {equivalence_classes(relation, domain)}")


dom = set(range(1, 9))
print(f"{'relation':>26} {'refl':>7} {'symm':>7} {'trans':>7} {'anti':>7}  kind")
describe("equality", {(a, a) for a in dom}, dom)
describe("same parity", {(a, b) for a in dom for b in dom if a % 2 == b % 2}, dom)
describe("a divides b", {(a, b) for a in dom for b in dom if b % a == 0}, dom)
describe("a is at most b", {(a, b) for a in dom for b in dom if a <= b}, dom)
describe("a is less than b", {(a, b) for a in dom for b in dom if a < b}, dom)
describe("differs by "
         "at most 1", {(a, b) for a in dom for b in dom if abs(a - b) <= 1}, dom)
