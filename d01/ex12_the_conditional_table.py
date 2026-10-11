"""The one row of the conditional that surprises everybody, and why it has to be that
way."""
from dmkit.logic import implies, truth_table

print("p implies q")
print(f"{'p':>7} {'q':>7} {'value':>7}   {'reading':<44}")
readings = {
    (False, False): "promise not tested: p never happened",
    (False, True): "promise not tested: p never happened",
    (True, False): "promise BROKEN: p happened and q did not",
    (True, True): "promise kept",
}
for a, v in truth_table(lambda p, q: implies(p, q), ["p", "q"]):
    key = (a["p"], a["q"])
    print(f"{str(a['p']):>7} {str(a['q']):>7} {str(v):>7}   {readings[key]:<44}")
print()
print("only one row is False, and it is the only row where the promise was tested and")
print("failed. A conditional with a false first "
      "part is true because nothing was claimed.")
print()
print(f"'if 2 + 2 = 5 then the moon is cheese' is {implies(False, False)}")
print(f"'if 2 + 2 = 5 then 1 = 1'              is {implies(False, True)}")
