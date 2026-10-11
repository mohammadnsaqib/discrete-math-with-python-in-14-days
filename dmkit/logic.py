"""Statements, truth tables, and deciding what follows from what. Day 1.

Everything in this module rests on one fact: a statement built from n variables has
exactly 2**n assignments, and 2**n is finite. So every question about it -- is it always
true, is it ever true, do these two agree -- is answered by building the table and
looking. No cleverness is needed and none is used here.

That is also the module's limit, and the book says so on the first page: 2**n is finite
but it doubles. Twenty variables is a million rows and thirty is a billion. Day 1 ends
at the point where looking stops being possible, which is where the rest of the subject
starts.
"""
from itertools import product


# --8<-- assignments
def assignments(names):
    """Every way of giving each name a truth value, in a fixed order.

    The order is not arbitrary and it is not `set` iteration: names are used exactly as
    given, and the values run False before True, so the table below reads like every
    printed truth table -- the last column alternating fastest. Two tables can only be
    compared row by row if both were built this way.
    """
    for values in product([False, True], repeat=len(names)):
        yield dict(zip(names, values))
# --8<--


# --8<-- evaluate
def evaluate(statement, assignment):
    """The truth value of a statement under one assignment.

    A statement is an ordinary Python function of keyword arguments, so `not`, `and` and
    `or` are Python's own. That is deliberate: the reader writes logic in the language
    they already have, and the only thing this module supplies is the exhaustive walk
    over assignments.
    """
    return bool(statement(**assignment))
# --8<--


# --8<-- truth_table
def truth_table(statement, names):
    """The whole table: one row per assignment, each row its values and the result.

    Its cost is 2**len(names) rows and there is no way round that. A tautology check on
    twelve variables is four thousand rows and runs in a moment; on thirty it is a
    billion and does not finish. Example 1.20 measures where the wall is.
    """
    return [(dict(a), evaluate(statement, a)) for a in assignments(names)]
# --8<--


# --8<-- is_tautology
def is_tautology(statement, names):
    """True when the statement holds under every assignment.

    This is a decision, not an estimate: the table is finite and every row was examined.
    It is the strongest thing said anywhere in this book by a computation alone, and it
    is only available because the domain is finite. Day 2 meets the first claim where it
    is not.
    """
    return all(result for _, result in truth_table(statement, names))
# --8<--


# --8<-- is_contradiction
def is_contradiction(statement, names):
    """True when the statement fails under every assignment."""
    return not any(result for _, result in truth_table(statement, names))
# --8<--


# --8<-- satisfiable
def satisfiable(statement, names):
    """The first assignment that makes the statement true, or None if there is none.

    Returning the assignment rather than a boolean is the whole point: a claim that
    something is satisfiable is checkable in one step if the witness comes with it, and
    unfalsifiable if it does not. Every routine in this book that answers "yes" returns
    the thing that made it so.
    """
    for a in assignments(names):
        if evaluate(statement, a):
            return dict(a)
    return None
# --8<--


# --8<-- models
def models(statement, names):
    """Every assignment under which the statement is true.

    The count of these is what Day 7 will call the size of an event, and what Day 14
    will read off a Karnaugh map. The same list answers three different chapters'
    questions.
    """
    return [dict(a) for a,
            result in [(a,
            evaluate(statement, a)) for a in assignments(names)]
            if result]
# --8<--


# --8<-- equivalent
def equivalent(first, second, names):
    """True when two statements have the same value under every assignment.

    Equivalence is a column comparison and nothing more. It needs no laws, no rewriting
    and no algebra -- which is why this book proves the laws of logic in section 1.7 by
    building both tables rather than by manipulating symbols.
    """
    return all(evaluate(first, a) == evaluate(second, a) for a in assignments(names))
# --8<--


# --8<-- entails
def entails(premises, conclusion, names):
    """True when every assignment satisfying all the premises also satisfies the
    conclusion.

    This is what an argument being valid means, and it says nothing about whether the
    premises are true. An argument from false premises to a false conclusion can be
    perfectly valid, and Example 1.14 tests four forms of argument.
    """
    for a in assignments(names):
        if all(evaluate(p, a) for p in premises) and not evaluate(conclusion, a):
            return False
    return True
# --8<--


# --8<-- to_cnf
def to_cnf(statement, names):
    """A conjunctive normal form for the statement, read straight off its false rows.

    Every row where the statement is FALSE forbids one assignment, and forbidding it is
    exactly one disjunction: the negation of that row. The conjunction of all of them is
    a conjunctive normal form. It is not the shortest one -- Day 14 minimises -- but it
    is correct by construction and needs no rewriting rules at all.

    The clauses come back as tuples of (name, expected) pairs, so a reader can check one
    by hand against the table without parsing a string.
    """
    clauses = []
    for a, result in truth_table(statement, names):
        if not result:
            clauses.append(tuple((n, not a[n]) for n in names))
    return clauses
# --8<--


# --8<-- cnf_text
def cnf_text(clauses):
    """A conjunctive normal form written out, for printing beside its table."""
    if not clauses:
        return "T"          # no false row: the statement is a tautology
    parts = []
    for clause in clauses:
        lits = [n if want else "not " + n for n, want in clause]
        parts.append("(" + " or ".join(lits) + ")")
    return " and ".join(parts)
# --8<--


def implies(p, q):
    """The conditional, as a function, because Python has no operator for it.

    Written out rather than as `not p or q` so that a reader meeting section 1.6 sees
    the definition and not an encoding of it.
    """
    return (not p) or q


def iff(p, q):
    """The biconditional: true exactly when both sides agree."""
    return p == q
