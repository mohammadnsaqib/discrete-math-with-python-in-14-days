"""Problem 14.27: which sets of gates can build every function, settled by closure."""
from dmkit.boolean import rows_of, truth_vector

ROWS = rows_of(3)


def closure(start, operations):
    """Every column reachable from the starting columns by the given operations.

    THE CLOSURE IS THE ANSWER. A set of gates builds a function exactly when that
    function's column turns up here, and the loop stops when nothing new appears, so the
    result is a fact about the gates rather than about how hard anybody tried.
    """
    found = set(start)
    growing = True
    while growing:
        growing = False
        for left in sorted(found):
            for right in sorted(found):
                for combine in operations:
                    made = tuple(combine(x, y) for x, y in zip(left, right))
                    if made not in found:
                        found.add(made)
                        growing = True
    return found


def is_monotone(vector):
    """True when turning an input from False to True never turns the output off."""
    index = {row: i for i, row in enumerate(ROWS)}
    return all(not (vector[index[row]] and not vector[index[row[:k] + (True,
               ) + row[k + 1:]]])
               for row in ROWS for k in range(3) if not row[k])


inputs = [truth_vector(lambda a, b, c, k=k: (a, b, c)[k], 3) for k in range(3)]
sets = [("and, or", [lambda x, y: x and y, lambda x, y: x or y]),
        ("and, or, not", [lambda x, y: x and y, lambda x, y: x or y,
                          lambda x, y: not x]),
        ("nand alone", [lambda x, y: not (x and y)]),
        ("nor alone", [lambda x, y: not (x or y)]),
        ("and alone", [lambda x, y: x and y]),
        ("or, not", [lambda x, y: x or y, lambda x, y: not x])]
print(f"{'gates allowed':>16} {'columns reachable':>20} {'all 256':>10}")
for name, operations in sets:
    reachable = closure(inputs, operations)
    print(f"{name:>16} {len(reachable):>20} {str(len(reachable) == 256):>10}")
print()
monotone = closure(inputs, [lambda x, y: x and y, lambda x, y: x or y])
count = sum(1 for column in range(256)
            if is_monotone(tuple(bool(column >> i & 1) for i in range(8))))
print(f"columns and-or can build                         : {len(monotone)}")
print(f"columns that never turn off when an input goes on: {count}")
print(f"the two constant columns are the difference      : "
      f"{len(monotone) == count - 2}")
print()
inverted = tuple(not v for v in inputs[0])
built = tuple(not (x and x) for x in inputs[0])
print(f"not a as a column     : {''.join('1' if v else '0' for v in inverted)}")
print(f"and-or can reach it   : {inverted in monotone}")
print(f"nand of a with itself : {''.join('1' if v else '0' for v in built)}, "
      f"the same column: {built == inverted}")
