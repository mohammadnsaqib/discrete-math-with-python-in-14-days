"""Problem 3.26: how many relations of each kind there are, by building all of them."""
from itertools import combinations

from dmkit.sets import (is_antisymmetric, is_reflexive, is_symmetric,
                        is_transitive)

print(f"{'n':>3} {'all relations':>14} {'reflexive':>11} {'symmetric':>11} "
      f"{'transitive':>12} {'equivalences':>13}")
for n in (1, 2, 3):
    dom = set(range(1, n + 1))
    all_pairs = [(a, b) for a in sorted(dom) for b in sorted(dom)]
    total = refl = symm = trans = equiv = 0
    for k in range(len(all_pairs) + 1):
        for chosen in combinations(all_pairs, k):
            rel = set(chosen)
            total += 1
            r, s, t = (is_reflexive(rel, dom), is_symmetric(rel), is_transitive(rel))
            refl += r
            symm += s
            trans += t
            equiv += r and s and t
    print(f"{n:>3} {total:>14} {refl:>11} {symm:>11} {trans:>12} {equiv:>13}")
