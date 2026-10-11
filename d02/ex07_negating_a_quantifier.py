"""Negating a quantifier turns it into the other one."""
from dmkit.proof import counterexample, exists, for_all, is_prime_slow

dom = range(2, 30)
pred = is_prime_slow

everything = for_all(pred, dom)
a_failure = counterexample(pred, dom)
print("claim   : every integer from 2 to 29 is prime")
print(f"holds   : {everything}")
print(f"not(for all) is the same as (there exists a failure)")
print(f"   not(for all P) = {not everything}")
print(f"   exists not-P   = {a_failure is not None}, witnessed by {a_failure}")
print()
some = exists(lambda n: n > 100, dom)
none_fail = for_all(lambda n: not (n > 100), dom)
print("claim   : some integer from 2 to 29 is above 100")
print(f"holds   : {some is not None}")
print(f"not(exists) is the same as (for all, not)")
print(f"   not(exists P) = {some is None}")
print(f"   for all not-P = {none_fail}")
