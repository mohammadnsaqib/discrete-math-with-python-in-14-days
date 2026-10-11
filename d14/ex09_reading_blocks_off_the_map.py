"""A block of adjacent True cells is a product term with letters missing."""
from dmkit.boolean import as_text, implicant_covers, karnaugh, minimise, truth_vector

cases = [("at least two of three",
          truth_vector(lambda a, b, c: sum([a, b, c]) >= 2, 3)),
         ("a alone decides", truth_vector(lambda a, b, c: a, 3)),
         ("an odd number",
          truth_vector(lambda a, b, c: sum([a, b, c]) % 2 == 1, 3))]
for name, vector in cases:
    m = karnaugh(vector, 3)
    print(f"{name}:")
    print("        " + "".join(f"{''.join('1' if x else '0' for x in c):>6}"
                               for c in m["cols"]))
    for label, row in zip(m["rows"], m["grid"]):
        text = "".join("1" if x else "0" for x in label)
        print(f"{text:>8}" + "".join(f"{('1' if v else '.'):>6}" for v in row))
    small = minimise(vector, 3)
    print(f"   the smallest expression: {as_text(small, ['a', 'b', 'c'])}")
    for pattern in small:
        shown = " ".join("-" if v is None else ("1" if v else "0") for v in pattern)
        print(f"      {shown} covers rows {implicant_covers(pattern, 3)}")
    print()
