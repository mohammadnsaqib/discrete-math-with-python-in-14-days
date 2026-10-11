"""A variable under a quantifier is not a variable any more."""
from dmkit.proof import exists, for_all, is_even

print("P(n): n is even")
print()
print("  P(n)                 -- a predicate. n is free, and there is no truth value.")
print(f"  for all n in 0..9    -- a statement. Its value is "
      f"{for_all(is_even, range(10))}.")
witness = exists(is_even, range(10))
print(f"  there exists n       -- a statement. Its value is {witness is not None}, "
      f"witnessed by {witness}.")
print()
print("the letter n means something different in each line. In the first it stands for")
print("whatever the reader supplies. In the "
      "other two it stands for nothing at all: the")
print("quantifier has used it up, and replacing every n by m changes no meaning.")
print()
print("that is why the two statements below say the same thing:")
print(f"   for all n in 0..9, n is even : {for_all(is_even, range(10))}")
print(f"   for all m in 0..9, m is even : {for_all(lambda m: is_even(m), range(10))}")
