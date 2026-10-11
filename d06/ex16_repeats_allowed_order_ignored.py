"""The fourth case, with the marks and dividers printed rather than described."""
from itertools import combinations_with_replacement

from dmkit.combin import combinations_count, combinations_with_repetition

kinds, picks = 3, 4
selections = list(combinations_with_replacement("abc", picks))

print(f"choosing {picks} from {kinds} kinds, order ignored, repeats allowed")
print(f"   by the rule  : {combinations_with_repetition(kinds, picks)}")
print(f"   by building  : {len(selections)}")
print()
print(f"{'selection':>12} {'as marks and dividers':>26}")
for s in selections[:8]:
    marks = "|".join("*" * s.count(ch) for ch in "abc")
    print(f"{''.join(s):>12} {marks:>26}")
print(f"{'...':>12} {f'{len(selections)} in all':>26}")
print()
print(f"every row is {picks} marks and {kinds - 1} dividers in a line, so there are "
      f"{picks + kinds - 1} places")
print(f"and {picks} of them hold a mark. That count is binomial({picks + kinds - 1}, "
      f"{picks}), which is {combinations_count(picks + kinds - 1, picks)}.")
