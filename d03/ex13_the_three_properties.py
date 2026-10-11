"""Reflexive, symmetric and transitive, checked on five relations."""
from dmkit.sets import is_reflexive, is_symmetric, is_transitive

dom = {1, 2, 3}
relations = [
    ("equality", {(1, 1), (2, 2), (3, 3)}),
    ("everything", {(a, b) for a in dom for b in dom}),
    ("nothing", set()),
    ("less than", {(a, b) for a in dom for b in dom if a < b}),
    ("at most", {(a, b) for a in dom for b in dom if a <= b}),
    ("differs by one", {(a, b) for a in dom for b in dom if abs(a - b) == 1}),
]
print(f"{'relation':>16} {'pairs':>6} {'reflexive':>11} {'symmetric':>11} "
      f"{'transitive':>12}")
for name, rel in relations:
    print(f"{name:>16} {len(rel):>6} {str(is_reflexive(rel, dom)):>11} "
          f"{str(is_symmetric(rel)):>11} {str(is_transitive(rel)):>12}")
