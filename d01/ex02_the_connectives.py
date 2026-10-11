"""The five connectives, and the whole of what each one means."""
from dmkit.logic import iff, implies

rows = [(False, False), (False, True), (True, False), (True, True)]
print(f"{'p':>6} {'q':>6} {'not p':>7} {'p and q':>9} {'p or q':>8} "
      f"{'p implies q':>13} {'p iff q':>9}")
for p, q in rows:
    print(f"{str(p):>6} {str(q):>6} {str(not p):>7} {str(p and q):>9} {str(p or q):>8} "
          f"{str(implies(p, q)):>13} {str(iff(p, q)):>9}")
