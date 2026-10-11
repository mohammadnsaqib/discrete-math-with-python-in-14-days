"""The same relation as a grid, which is where Day 11 picks it up."""
from dmkit.sets import cartesian

dom = [1, 2, 3, 4]
divides = {(a, b) for a in dom for b in dom if b % a == 0}

print("b % a == 0, drawn as a grid. Row a, column b.")
print("      " + " ".join(f"{b:>3}" for b in dom))
for a in dom:
    row = " ".join("  1" if (a, b) in divides else "  ." for b in dom)
    print(f"  {a:>3} {row}")
print()
print(f"pairs in the relation : {len(divides)} of {len(cartesian(dom, dom))}")
print(f"on the diagonal       : {sum(1 for a in dom if (a, a) in divides)}")
