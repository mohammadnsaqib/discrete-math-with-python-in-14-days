"""Boolean functions, the circuits that build them, and the machines that read. Day 14.

Day 1 built truth tables and read them. Today writes them: given a column of outputs,
produce a statement that has exactly that column, then make it smaller.

A BOOLEAN FUNCTION IS ITS TRUTH TABLE AND NOTHING ELSE. Two expressions that look
nothing alike are the same function when their columns match, and `truth_vector` is what
settles it. Every simplification in this module is checked that way rather than by
rewriting rules, because a rewriting rule applied wrongly produces a different function
that still looks plausible.

THE MINIMISATION HERE IS A SEARCH, over every sum of products up to a size. It is
exponential and it is honest: the fast methods are approximations, and Example 14.7
measures the gap.
"""
from itertools import combinations, product


# --8<-- truth_vector
def truth_vector(function, arity):
    """The output column of a function, over every input row in a fixed order.

    THE ORDER IS THE WHOLE POINT. Rows run from all-False to all-True as if the inputs
    were the bits of a counting number, so two functions have the same vector exactly
    when they are the same function.
    """
    return tuple(bool(function(*row))
                 for row in product([False, True], repeat=arity))
# --8<--


# --8<-- rows_of
def rows_of(arity):
    """Every input row, in the order truth_vector uses."""
    return list(product([False, True], repeat=arity))
# --8<--


# --8<-- same_function
def same_function(left, right, arity):
    """True when two functions have the same output column."""
    return truth_vector(left, arity) == truth_vector(right, arity)
# --8<--


# --8<-- minterms
def minterms(vector):
    """The rows where the function is True, as indices into the row order."""
    return [i for i, value in enumerate(vector) if value]
# --8<--


# --8<-- sum_of_products
def sum_of_products(vector, names=None):
    """An expression with exactly this output column, built one True row at a time.

    Each True row contributes one product that is True on that row and nowhere else.
    Adding them gives a function True on exactly those rows, which is the column asked
    for. The result is correct and usually far from smallest -- `minimise` is the
    routine for that.
    """
    arity = len(vector).bit_length() - 1
    names = names or [chr(ord("a") + i) for i in range(arity)]
    rows = rows_of(arity)
    terms = []
    for i in minterms(vector):
        parts = [names[k] if rows[i][k] else f"not {names[k]}" for k in range(arity)]
        terms.append(" and ".join(parts))
    if not terms:
        return "False"
    if len(terms) == len(vector):
        return "True"
    return " or ".join(f"({t})" for t in terms)
# --8<--


# --8<-- implicant_covers
def implicant_covers(pattern, arity):
    """The rows a product term covers, given a pattern of True, False and None.

    A `None` means the input does not appear in the term, so the term covers both values
    of it. That is how a product with fewer letters covers more rows, and it is the
    whole mechanism behind making an expression smaller.
    """
    rows = rows_of(arity)
    return [i for i, row in enumerate(rows)
            if all(p is None or p == row[k] for k, p in enumerate(pattern))]
# --8<--


# --8<-- all_implicants
def all_implicants(vector, arity):
    """Every product term that is True only on rows where the function is True."""
    wanted = set(minterms(vector))
    found = []
    for pattern in product([None, False, True], repeat=arity):
        covered = implicant_covers(pattern, arity)
        if covered and set(covered) <= wanted:
            found.append(pattern)
    return found
# --8<--


# --8<-- prime_implicants
def prime_implicants(vector, arity):
    """The implicants that no larger implicant swallows.

    A term whose rows are all covered by a bigger term is never needed: swapping the
    bigger one in covers at least as much with fewer letters. Searching over these
    instead of over every implicant is EXACT and far smaller -- at four inputs it turns
    a search that runs for a minute into one that finishes at once.
    """
    found = all_implicants(vector, arity)
    covers = {p: set(implicant_covers(p, arity)) for p in found}
    return [p for p in found
            if not any(q is not p and covers[p] < covers[q] for q in found)]
# --8<--


# --8<-- minimise
def minimise(vector, arity):
    """The smallest set of product terms covering every True row, found by search.

    Smallest by the count of terms, then by the total count of letters, then by a
    printed form of the patterns so that two runs return the same answer. THE SEARCH IS
    EXPONENTIAL in the number of prime implicants and no approximation is used, because
    an approximation would oblige the book to say how close it was.
    """
    wanted = set(minterms(vector))
    if not wanted:
        return []
    implicants = prime_implicants(vector, arity)
    for size in range(1, len(implicants) + 1):
        best = None
        for chosen in combinations(implicants, size):
            covered = set()
            for pattern in chosen:
                covered.update(implicant_covers(pattern, arity))
            if covered == wanted:
                letters = sum(1 for p in chosen for x in p if x is not None)
                # THE SECOND KEY IS A STRING, not the patterns themselves. A pattern
                # holds None as well as True and False, and Python refuses to order None
                # against a bool, so sorting on the raw tuples raises rather than
                # choosing.
                shape = "".join("-" if x is None else ("1" if x else "0")
                                for p in chosen for x in p)
                key = (letters, shape)
                if best is None or key < best[0]:
                    best = (key, chosen)
        if best is not None:
            return list(best[1])
    return []
# --8<--


# --8<-- as_text
def as_text(patterns, names=None):
    """A list of product patterns written out as an expression."""
    if not patterns:
        return "False"
    arity = len(patterns[0])
    names = names or [chr(ord("a") + i) for i in range(arity)]
    terms = []
    for pattern in patterns:
        parts = [names[k] if value else f"not {names[k]}"
                 for k, value in enumerate(pattern) if value is not None]
        terms.append(" and ".join(parts) if parts else "True")
    return " or ".join(f"({t})" for t in terms)
# --8<--


# --8<-- evaluate_patterns
def evaluate_patterns(patterns, row):
    """Whether a sum of product terms is True on one input row."""
    for pattern in patterns:
        if all(value is None or value == row[k] for k, value in enumerate(pattern)):
            return True
    return False
# --8<--


# --8<-- karnaugh
def karnaugh(vector, arity):
    """The truth table laid out so that neighbouring cells differ in one input.

    The layout is the reason the map is useful: a block of adjacent True cells is
    exactly a product term with some inputs missing. This returns the grid and its row
    and column labels; reading the blocks off it is the reader's job and `minimise` is
    the machine's.
    """
    if arity not in (2, 3, 4):
        raise ValueError("a Karnaugh map is drawn for two, three or four inputs")
    gray2 = [(False, False), (False, True), (True, True), (True, False)]
    if arity == 2:
        row_bits, col_bits = [(False,), (True,)], [(False,), (True,)]
    elif arity == 3:
        row_bits, col_bits = [(False,), (True,)], gray2
    else:
        row_bits, col_bits = gray2, gray2
    rows = rows_of(arity)
    index = {row: i for i, row in enumerate(rows)}
    grid = [[vector[index[r + c]] for c in col_bits] for r in row_bits]
    return {"grid": grid, "rows": row_bits, "cols": col_bits}
# --8<--


# --8<-- circuit_depth
def circuit_depth(patterns):
    """How many layers of gates a sum of products needs.

    One layer inverts the inputs that need it, one forms each product, and one adds
    them. A product of one letter needs no AND layer and a sum of one term needs no OR
    layer, which is why this counts rather than returning three.
    """
    if not patterns:
        return 0
    needs_not = any(value is False for pattern in patterns for value in pattern)
    widest = max(sum(1 for v in pattern if v is not None) for pattern in patterns)
    depth = 1 if needs_not else 0
    if widest > 1:
        depth += 1
    if len(patterns) > 1:
        depth += 1
    return depth
# --8<--


# --8<-- gate_count
def gate_count(patterns):
    """How many gates a sum of products needs, counted by kind."""
    if not patterns:
        return {"not": 0, "and": 0, "or": 0}
    inverted = {k for pattern in patterns for k, v in enumerate(pattern) if v is False}
    ands = sum(1 for p in patterns if sum(1 for v in p if v is not None) > 1)
    return {"not": len(inverted), "and": ands,
            "or": 1 if len(patterns) > 1 else 0}
# --8<--


# --8<-- StateMachine
class StateMachine:
    """A finite state machine: states, a start, some accepting states, and a move table.

    The move table is a dictionary from (state, symbol) to state. A missing entry is a
    REFUSAL rather than a crash, so a machine can be given an alphabet it does not fully
    handle and still say no.
    """

    def __init__(self, states, start, accepting, moves):
        self.states = sorted(states)
        self.start = start
        self.accepting = set(accepting)
        self.moves = dict(moves)

    def run(self, word):
        """The states the machine passes through, ending in None if it refuses."""
        trail = [self.start]
        state = self.start
        for symbol in word:
            state = self.moves.get((state, symbol))
            trail.append(state)
            if state is None:
                break
        return trail

    def accepts(self, word):
        """True when the machine ends in an accepting state."""
        trail = self.run(word)
        return trail[-1] in self.accepting
# --8<--


def all_words(alphabet, longest):
    """Every word up to the given length, shortest first, in a fixed order."""
    out = [""]
    for length in range(1, longest + 1):
        out.extend("".join(t) for t in product(sorted(alphabet), repeat=length))
    return out
