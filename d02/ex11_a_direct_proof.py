"""A direct proof, and the finite check that agrees with it."""
from dmkit.proof import direct_check, divides, is_even

# CLAIM. If n is divisible by 6 then n is divisible by 3. PROOF. n divisible by 6 means
# n = 6k for some integer k. Then n = 3(2k), and 2k is an integer, so 3 divides n. That
# argument used no property of n except the one assumed, so it holds for every integer
# -- which is what a proof is and what the check below is not.
result = direct_check(lambda n: divides(6, n), lambda n: divides(3, n), range(1, 601))
print("claim: if 6 divides n then 3 divides n")
print(f"   members where the hypothesis held : {result['tested']}")
print(f"   of those, the conclusion failed on: {result['failures']}")
print(f"   members the hypothesis skipped    : {result['vacuous']}")
