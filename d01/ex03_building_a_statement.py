"""One compound statement, taken apart at one assignment."""
from dmkit.logic import implies

p, q, r = True, False, True
print(f"p = {p}, q = {q}, r = {r}")
print()
print(f"  not q                    = {not q}")
print(f"  p and (not q)            = {p and (not q)}")
print(f"  q or r                   = {q or r}")
print(f"  (p and not q) implies (q or r) = {implies(p and (not q), q or r)}")
