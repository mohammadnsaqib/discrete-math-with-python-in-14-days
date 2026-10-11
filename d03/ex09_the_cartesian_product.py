"""Ordered pairs, and why the product is not a union."""
from dmkit.sets import as_text, cartesian

A = {1, 2, 3}
B = {"x", "y"}
pairs = cartesian(A, B)
print(f"A = {as_text(A)}, B = {as_text(B)}")
print(f"A x B has {len(pairs)} pairs: {pairs}")
print()
reverse = cartesian(B, A)
print(f"B x A has {len(reverse)} pairs: {reverse}")
print(f"the two are equal: {pairs == reverse}")
print()
print(f"|A| x |B| = {len(A)} x {len(B)} = {len(A) * len(B)}, and the product has "
      f"{len(pairs)}.")
print()
triples = [(a, b, c) for a in sorted(A) for b in sorted(B) for c in sorted(A)]
print(f"A x B x A has {len(triples)}, which is {len(A)} x {len(B)} x {len(A)}.")
print("the sizes multiply because each position is chosen independently of the others.")
