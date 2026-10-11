"""Induction does not need numbers. It needs a base and a way to build."""
from itertools import product

# A LIST IS DEFINED RECURSIVELY: it is empty, or it is one item followed by a list.
# Every claim about lists is then proved the same way a claim about numbers is -- check
# the empty list, and check that adding one item in front preserves the claim.


def length_rec(xs):
    """The length of a list, read off its recursive definition."""
    if not xs:
        return 0
    return 1 + length_rec(xs[1:])


def append_rec(xs, ys):
    """One list followed by another, built by walking the first."""
    if not xs:
        return ys
    return (xs[0],) + append_rec(xs[1:], ys)


def reverse_rec(xs):
    """A list turned around, one item at a time."""
    if not xs:
        return ()
    return reverse_rec(xs[1:]) + (xs[0],)


shorts = [tuple(t) for k in range(5) for t in product("ab", repeat=k)]
print(f"{len(shorts)} lists of length 0 to 4 over two items")
print()
print(f"{'xs':>17} {'ys':>12} {'xs + ys':>27} {'lengths add':>12}")
for xs, ys in [((), ()), (("a",), ()), (("a", "b"), ("a",)),
               (("b", "a", "b"), ("a", "a"))]:
    joined = append_rec(xs, ys)
    ok = length_rec(joined) == length_rec(xs) + length_rec(ys)
    print(f"{str(xs):>17} {str(ys):>12} {str(joined):>27} {str(ok):>12}")
print()
bad_len = [(xs, ys) for xs in shorts for ys in shorts
           if length_rec(append_rec(xs, ys)) != length_rec(xs) + length_rec(ys)]
bad_rev = [xs for xs in shorts if reverse_rec(reverse_rec(xs)) != xs]
print(f"pairs among {len(shorts) ** 2} where the lengths did not add: {len(bad_len)}")
print(f"lists where reversing twice did not return the original: {len(bad_rev)}")
