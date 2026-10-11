"""Two arguments of the same shape, one of which is valid."""
from dmkit.logic import assignments, entails, evaluate, implies

names = ["p", "q"]
conditional = lambda p, q: implies(p, q)

arguments = [
    ("from (p implies q) and p, conclude q", [conditional, lambda p, q: p],
     lambda p, q: q),
    ("from (p implies q) and q, conclude p", [conditional, lambda p, q: q],
     lambda p, q: p),
    ("from (p implies q) and not q, conclude not p", [conditional, lambda p, q: not q],
     lambda p, q: not p),
    ("from (p implies q) and not p, conclude not q", [conditional, lambda p, q: not p],
     lambda p, q: not q),
]
for text, premises, conclusion in arguments:
    valid = entails(premises, conclusion, names)
    print(f"{text:<48} valid: {valid}")
    if not valid:
        for a in assignments(names):
            if all(evaluate(p, a) for p in premises) and not evaluate(conclusion, a):
                shown = ", ".join(f"{k}={str(v)}" for k, v in a.items())
                print(f"{'':<48} broken at {shown}")
                break
