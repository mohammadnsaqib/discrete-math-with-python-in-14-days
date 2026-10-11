"""The truth table laid out so that neighbours differ in one input."""
from dmkit.boolean import karnaugh, minterms, truth_vector

alarm = truth_vector(lambda a, b, c: sum([a, b, c]) >= 2, 3)
m = karnaugh(alarm, 3)
labels = ["".join("1" if x else "0" for x in c) for c in m["cols"]]
print("at least two of three, as a map with a down the side and b, c across:")
print("        " + "".join(f"{c:>6}" for c in labels))
for label, row in zip(m["rows"], m["grid"]):
    text = "".join("1" if x else "0" for x in label)
    print(f"{text:>8}" + "".join(f"{('1' if v else '.'):>6}" for v in row))
print()
print(f"the True rows: {minterms(alarm)}")
print(f"the column labels in order: {labels}")
steps = [sum(1 for x, y in zip(m["cols"][i], m["cols"][i + 1]) if x != y)
         for i in range(len(m["cols"]) - 1)]
print(f"neighbouring columns differ in: {steps} input")
print(f"and the last and first differ in: "
      f"{sum(1 for x, y in zip(m['cols'][-1], m['cols'][0]) if x != y)}")
