"""Two expressions with one column, and the shorter one found by search."""
from dmkit.boolean import (as_text, evaluate_patterns, minimise, minterms, rows_of,
                           sum_of_products)

cases = [("at least "
          "two of three", (False, False, False, True, False, True, True, True)),
         ("a alone decides", (False, False, False, False, True, True, True, True)),
         ("an odd number", (False, True, True, False, True, False, False, True)),
         ("all three", (False,) * 7 + (True,)),
         ("never", (False,) * 8)]
faults = 0
print(f"{'function':>24} {'terms from the rows':>21} {'terms after search':>20} "
      f"{'letters saved':>15}")
for name, vector in cases:
    plain = [rows_of(3)[i] for i in minterms(vector)]
    small = minimise(vector, 3)
    saved = (sum(1 for p in plain for v in p if v is not None)
             - sum(1 for p in small for v in p if v is not None))
    faults += tuple(evaluate_patterns(small, r) for r in rows_of(3)) != vector
    print(f"{name:>24} {len(plain):>21} {len(small):>20} {saved:>15}")
print()
print(f"smaller expressions whose column changed: {faults}")
print()
for name, vector in cases[:3]:
    print(f"{name}:")
    print(f"   from the rows: {sum_of_products(vector, ['a', 'b', 'c'])}")
    print(f"   after search : {as_text(minimise(vector, 3), ['a', 'b', 'c'])}")
