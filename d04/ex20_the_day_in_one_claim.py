"""Every piece of the day, applied to one claim about a set defined recursively."""
from itertools import product

# THE SET OF BALANCED STRINGS is defined recursively: the empty string is balanced; if s
# and t are balanced then so are "(" + s + ")" and s + t. The claim is that every
# balanced string has as many closers as openers and never closes one it has not opened.


def build(depth, longest=8):
    """Every balanced string the definition reaches within the given number of steps.

    The two building rules are applied over and over, and nothing longer than `longest`
    is kept -- the definition reaches infinitely many strings, and a program can only
    print a finite piece of any set.
    """
    known = {""}
    for _ in range(depth):
        known |= {"(" + s + ")" for s in known if len(s) + 2 <= longest}
        known |= {s + t for s in known for t in known if len(s) + len(t) <= longest}
    return sorted(known, key=lambda s: (len(s), s))


def is_balanced(s):
    """The property claimed: counts match, and no prefix has more closers than openers.
    """
    depth = 0
    for ch in s:
        depth += 1 if ch == "(" else -1
        if depth < 0:
            return False
    return depth == 0


built = build(4)
print(f"strings the definition reaches, up to length 8: {len(built)}")
print(f"the first twelve: {built[:12]}")
print()
unbalanced = [s for s in built if not is_balanced(s)]
print(f"of those, how many are not balanced: {len(unbalanced)}")
print()
everything = ["".join(t) for k in range(0, 9, 2) for t in product("()", repeat=k)]
missed = [s for s in everything if is_balanced(s) and s not in built]
print(f"balanced strings of length up to 8 the definition did NOT reach: {len(missed)}")
print()
counts = [len([s for s in built if len(s) == 2 * n]) for n in range(5)]
assert sum(counts) == len(built)
print(f"{'half length':>12} {'balanced strings':>18}")
for n, c in enumerate(counts):
    print(f"{n:>12} {c:>18}")
print()
print(f"the counts are the Catalan numbers, which Day 8 derives: {counts}")
