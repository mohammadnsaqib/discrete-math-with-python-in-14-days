"""Problem 1.25: a table printer that takes any statement and names its own columns."""
from dmkit.logic import assignments, evaluate, implies


def show(title, statement, names, parts=()):
    """Print a table with one column per named intermediate part, then the whole
    statement.

    The intermediate columns are the point. A table of only the final value says whether
    a statement holds; a table with its parts beside it says WHERE it stopped holding.

    Each column is made as wide as its own heading and no wider. A fixed width looks
    tidy until one heading is longer than it, and then two columns run together with
    nothing to say they have."""
    heads = list(names) + [label for label, _ in parts] + [title]
    widths = [max(len(h), 6) + 2 for h in heads]
    print("  " + "".join(f"{h:>{w}}" for h, w in zip(heads, widths)))
    for a in assignments(names):
        cells = [str(a[n]) for n in names]
        cells += [str(evaluate(f, a)) for _, f in parts]
        cells.append(str(evaluate(statement, a)))
        print("  " + "".join(f"{c:>{w}}" for c, w in zip(cells, widths)))


show("(p or q) implies (p and q)",
     lambda p, q: implies(p or q, p and q),
     ["p", "q"],
     parts=[("p or q", lambda p, q: p or q), ("p and q", lambda p, q: p and q)])
print()
show("not (p and (q or not r))",
     lambda p, q, r: not (p and (q or (not r))),
     ["p", "q", "r"],
     parts=[("q or not r", lambda p, q, r: q or (not r))])
