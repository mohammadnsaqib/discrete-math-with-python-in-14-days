"""Four statements from one conditional, and only two of them agree."""
from dmkit.logic import assignments, equivalent, evaluate, implies

forms = {
    "p implies q       (the conditional)": lambda p, q: implies(p, q),
    "q implies p       (the converse)": lambda p, q: implies(q, p),
    "not p implies not q  (the inverse)": lambda p, q: implies(not p, not q),
    "not q implies not p  (the contrapositive)": lambda p, q: implies(not q, not p),
}
names = ["p", "q"]
print(f"{'p':>6} {'q':>6}" + "".join(f"{k.split('(')[0].strip():>22}" for k in forms))
for a in assignments(names):
    row = "".join(f"{str(evaluate(f, a)):>22}" for f in forms.values())
    print(f"{str(a['p']):>6} {str(a['q']):>6}{row}")
print()
keys = list(forms)
for i in range(len(keys)):
    for j in range(i + 1, len(keys)):
        if equivalent(forms[keys[i]], forms[keys[j]], names):
            print(f"equivalent: {keys[i].split('(')[1][:-1]} and "
                  f"{keys[j].split('(')[1][:-1]}")
