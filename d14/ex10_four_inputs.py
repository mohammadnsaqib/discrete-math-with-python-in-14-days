"""A map of four inputs, and how much it saves."""
from dmkit.boolean import karnaugh, minimise, minterms, truth_vector

divisible = truth_vector(
    lambda a, b, c, d: (8 * a + 4 * b + 2 * c + d) % 3 == 0 and (a or b or c or d), 4)
m = karnaugh(divisible, 4)
print("a four-bit number divisible by 3, with a, b down the side and c, d across:")
print("        " + "".join(f"{''.join('1' if x else '0' for x in c):>6}"
                           for c in m["cols"]))
for label, row in zip(m["rows"], m["grid"]):
    text = "".join("1" if x else "0" for x in label)
    print(f"{text:>8}" + "".join(f"{('1' if v else '.'):>6}" for v in row))
print()
print(f"the True rows: {minterms(divisible)}")
print()
cases = [("divisible by 3", divisible),
         ("at least two of four",
          truth_vector(lambda a, b, c, d: sum([a, b, c, d]) >= 2, 4)),
         ("an odd number set",
          truth_vector(lambda a, b, c, d: sum([a, b, c, d]) % 2 == 1, 4)),
         ("a and b agree", truth_vector(lambda a, b, c, d: a == b, 4))]
print(f"{'function':>26} {'True rows':>11} {'terms from rows':>17} "
      f"{'after search':>14} {'saved':>7}")
for name, vector in cases:
    small = minimise(vector, 4)
    print(f"{name:>26} {len(minterms(vector)):>11} {len(minterms(vector)):>17} "
          f"{len(small):>14} {len(minterms(vector)) - len(small):>7}")
