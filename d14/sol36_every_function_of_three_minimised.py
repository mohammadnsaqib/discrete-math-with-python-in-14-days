"""Problem 14.25: minimise all 256 functions of three inputs and check every one."""
from sympy import symbols
from sympy.logic.boolalg import And, Or, SOPform, simplify_logic

from dmkit.boolean import (as_text, evaluate_patterns, minimise, minterms, rows_of,
                           sum_of_products)

NAMES = symbols("a b c")


def shape_of(expression):
    """The count of terms and the count of letters in a SymPy expression."""
    if expression in (True, False):
        return (0 if expression is False else 1, 0)
    terms = expression.args if isinstance(expression, Or) else (expression,)
    return (len(terms), sum(len(t.args) if isinstance(t, And) else 1 for t in terms))


def sympy_answer(vector):
    """SymPy's own smallest sum of products for the same column."""
    wanted = minterms(vector)
    return False if not wanted else simplify_logic(SOPform(list(NAMES), wanted),
                                                   form="dnf")


rows = rows_of(3)
tally = {}
wrong = fewer_here = fewer_there = 0
for column in range(256):
    vector = tuple(bool(column >> i & 1) for i in range(8))
    chosen = minimise(vector, 3)
    wrong += tuple(evaluate_patterns(chosen, row) for row in rows) != vector
    mine = (len(chosen), sum(1 for p in chosen for x in p if x is not None))
    theirs = shape_of(sympy_answer(vector))
    fewer_here += mine[0] < theirs[0]
    fewer_there += theirs[0] < mine[0]
    tally[mine[0]] = tally.get(mine[0], 0) + 1
print("functions of three inputs tested       : 256")
print(f"minimised columns that did not match   : {wrong}")
print(f"functions where this book used fewer   : {fewer_here}")
print(f"functions where SymPy used fewer terms : {fewer_there}")
print()
print(f"{'terms':>8} {'functions':>12}")
for key in sorted(tally):
    print(f"{key:>8} {tally[key]:>12}")
print()
worst = max(range(256), key=lambda c: len(minimise(
    tuple(bool(c >> i & 1) for i in range(8)), 3)))
vector = tuple(bool(worst >> i & 1) for i in range(8))
print(f"the column needing the most terms: "
      f"{''.join('1' if v else '0' for v in vector)}")
print(f"   the smallest found: {as_text(minimise(vector, 3))}")
print(f"   SymPy's answer    : {sympy_answer(vector)}")
