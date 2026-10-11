"""What finding the smallest expression costs, and what a quick rule gets instead."""
from itertools import product

from dmkit.boolean import (all_implicants, as_text, evaluate_patterns,
                           implicant_covers, minimise, minterms, rows_of)


def greedy_cover(vector, arity):
    """A cover built by taking the term that covers the most uncovered rows, over and
    over."""
    left, chosen = set(minterms(vector)), []
    pool = all_implicants(vector, arity)
    while left:
        best = max(pool, key=lambda p: (len(left & set(implicant_covers(p, arity))),
                                        -sum(1 for v in p if v is not None)))
        chosen.append(best)
        left -= set(implicant_covers(best, arity))
    return chosen


worse = tested = faults = 0
worst = None
for vector in product([False, True], repeat=8):
    small = minimise(vector, 3)
    faults += tuple(evaluate_patterns(small, r) for r in rows_of(3)) != vector
    if not any(vector):
        continue
    tested += 1
    quick = greedy_cover(vector, 3)
    if len(quick) > len(small):
        worse += 1
        if worst is None or len(quick) - len(small) > worst[0]:
            worst = (len(quick) - len(small), vector, quick, small)
print(f"functions of 3 inputs with at least one True row: {tested}")
print(f"the quick rule matched the search on : {tested - worse}")
print(f"the quick rule used more terms on    : {worse}")
print(f"minimised expressions whose column changed: {faults}")
print()
print(f"the worst gap was {worst[0]} term, on the column {worst[1]}")
print(f"   the quick rule: {as_text(worst[2], ['a', 'b', 'c'])}")
print(f"   the search    : {as_text(worst[3], ['a', 'b', 'c'])}")
