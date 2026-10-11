"""A product with one letter missing covers twice as many rows."""
from dmkit.boolean import all_implicants, implicant_covers, minterms

arity = 3
vector = (False, False, False, True, False, True, True, True)
wanted = set(minterms(vector))
print(f"the function is True on rows {sorted(wanted)}")
print()
print(f"{'pattern':>24} {'letters':>9} {'rows it covers':>18} "
      f"{'inside the function':>21}")
for pattern in ((True, True, True), (None, True, True), (True, None, True),
                (True, True, None), (True, None, None), (None, None, None)):
    covered = implicant_covers(pattern, arity)
    letters = sum(1 for v in pattern if v is not None)
    shown = " ".join("-" if v is None else ("1" if v else "0") for v in pattern)
    print(f"{shown:>24} {letters:>9} {str(covered):>18} "
          f"{str(set(covered) <= wanted):>21}")
print()
usable = all_implicants(vector, arity)
by_letters = {}
for pattern in usable:
    letters = sum(1 for v in pattern if v is not None)
    by_letters[letters] = by_letters.get(letters, 0) + 1
print(f"product terms that stay inside the function: {len(usable)}")
print(f"{'letters':>9} {'rows each covers':>18} {'how many there are':>20}")
for letters in sorted(by_letters):
    print(f"{letters:>9} {2 ** (arity - letters):>18} {by_letters[letters]:>20}")
