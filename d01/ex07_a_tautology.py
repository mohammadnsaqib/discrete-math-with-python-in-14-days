"""A statement true under every assignment, and the table that settles it."""
from dmkit.logic import implies, is_tautology, truth_table


def excluded_middle(p):
    """p or not p."""
    return p or (not p)


def modus_ponens_form(p, q):
    """((p implies q) and p) implies q."""
    return implies(implies(p, q) and p, q)


print("p or not p")
for a, v in truth_table(excluded_middle, ["p"]):
    print(f"   p = {str(a['p']):<6} -> {v}")
print(f"   tautology: {is_tautology(excluded_middle, ['p'])}")
print()
print("((p implies q) and p) implies q")
for a, v in truth_table(modus_ponens_form, ["p", "q"]):
    print(f"   p = {str(a['p']):<6} q = {str(a['q']):<6} -> {v}")
print(f"   tautology: {is_tautology(modus_ponens_form, ['p', 'q'])}")
