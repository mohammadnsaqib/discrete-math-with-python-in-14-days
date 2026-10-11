"""Reading the negation of a claim off the claim, and checking both against a search."""
from dmkit.proof import counterexample, exists, is_prime_slow

dom = range(2, 200)

print("claim   : every integer from 2 to 199 is prime")
print("negation: some integer from 2 to 199 is not prime")
w = counterexample(is_prime_slow, dom)
print(f"   the claim holds   : False")
print(f"   the negation holds: True, witnessed by {w}")
print()
print("claim   : some integer from 2 to 199 is divisible by 97 and by 89")
print("negation: every integer from 2 to 199 fails to be divisible by both")
both = exists(lambda n: n % 97 == 0 and n % 89 == 0, dom)
print(f"   the claim holds   : {both is not None}")
print(f"   the negation holds: {both is None}")
