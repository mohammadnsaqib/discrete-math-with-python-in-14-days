"""Problem 14.26: what minimising saves, counted in gates rather than in letters."""
from dmkit.boolean import circuit_depth, gate_count, minimise, minterms, rows_of


def patterns_of(vector, arity):
    """One product pattern per True row, which is what sum_of_products builds."""
    rows = rows_of(arity)
    return [tuple(rows[i]) for i in minterms(vector)]


def total(counts):
    """Gates of every kind added together."""
    return counts["not"] + counts["and"] + counts["or"]


saved = same = deeper = before_all = after_all = 0
best = (0, None)
for column in range(256):
    vector = tuple(bool(column >> i & 1) for i in range(8))
    plain, small = patterns_of(vector, 3), minimise(vector, 3)
    before, after = total(gate_count(plain)), total(gate_count(small))
    before_all += before
    after_all += after
    saved += before - after
    same += before == after
    deeper += circuit_depth(small) > circuit_depth(plain)
    # THE CONSTANT COLUMNS ARE SET ASIDE. All-True and all-False collapse to no gates at
    # all, which is a true saving and an uninteresting one.
    if 0 < sum(vector) < 8 and before - after > best[0]:
        best = (before - after, vector)
print(f"{'gates before minimising, in all':>34}: {before_all}")
print(f"{'gates after minimising, in all':>34}: {after_all}")
print(f"{'gates saved':>34}: {saved}")
print(f"{'functions that saved nothing':>34}: {same}")
print(f"{'circuits that came out deeper':>34}: {deeper}")
print()
vector = best[1]
plain, small = patterns_of(vector, 3), minimise(vector, 3)
print(f"the best saving on a column that is not constant: {best[0]} gates")
print(f"   the column: {''.join('1' if v else '0' for v in vector)}")
print(f"{'':>14} {'not':>6} {'and':>6} {'or':>6} {'total':>7} {'layers':>8}")
for label, patterns in (("one per row", plain), ("minimised", small)):
    c = gate_count(patterns)
    print(f"{label:>14} {c['not']:>6} {c['and']:>6} {c['or']:>6} "
          f"{total(c):>7} {circuit_depth(patterns):>8}")
