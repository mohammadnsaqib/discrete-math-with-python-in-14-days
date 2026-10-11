"""A statement false under every assignment."""
from dmkit.logic import is_contradiction, is_tautology, truth_table


def never(p):
    """p and not p."""
    return p and (not p)


def also_never(p, q):
    """(p and q) and (not p)."""
    return (p and q) and (not p)


for name, st, names in (("p and not p", never, ["p"]),
                        ("(p and q) and not p", also_never, ["p", "q"])):
    print(name)
    for a, v in truth_table(st, names):
        shown = "  ".join(f"{k} = {str(val):<6}" for k, val in a.items())
        print(f"   {shown} -> {v}")
    print(f"   contradiction: {is_contradiction(st, names)}, "
          f"tautology: {is_tautology(st, names)}")
    print()
print("a contradiction is not a mistake. It is "
      "a statement, and its table is all False.")
