"""Proving the contrapositive instead, and the check that both forms agree."""
from dmkit.proof import direct_check, is_even, is_odd

# CLAIM. If n squared is even then n is even. The direct route is awkward: knowing n^2 =
# 2k says little about n. The contrapositive is immediate: if n is ODD then n = 2a+1, so
# n^2 = 4a^2+4a+1, which is odd. Day 1 showed the two forms are equivalent, so proving
# either proves both.
dom = range(1, 401)
direct = direct_check(lambda n: is_even(n * n), lambda n: is_even(n), dom)
contra = direct_check(lambda n: is_odd(n), lambda n: is_odd(n * n), dom)

print("claim          : if n squared is even then n is even")
print(f"   tested on   : {direct['tested']} members, failures {direct['failures']}")
print()
print("contrapositive : if n is odd then n squared is odd")
print(f"   tested on   : {contra['tested']} members, failures {contra['failures']}")
