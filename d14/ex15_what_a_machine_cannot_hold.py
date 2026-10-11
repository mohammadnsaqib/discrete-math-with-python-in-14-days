"""A finite machine holds finitely much, and some rules need more."""
from dmkit.boolean import StateMachine, all_words


def machine_for_depth(limit):
    """Accepts balanced brackets nested no deeper than the limit, and no others.

    Each state is a depth. A machine with a fixed number of states can only count that
    far, which is the whole point: raising the limit needs another state.
    """
    moves = {}
    for d in range(limit + 1):
        if d + 1 <= limit:
            moves[(d, "(")] = d + 1
        if d - 1 >= 0:
            moves[(d, ")")] = d - 1
    return StateMachine(list(range(limit + 1)), 0, [0], moves)


def balanced(word):
    """True when the brackets match, checked with a counter and no state limit."""
    depth = 0
    for ch in word:
        depth += 1 if ch == "(" else -1
        if depth < 0:
            return False
    return depth == 0


words = all_words("()", 8)
print(f"{'states':>8} {'deepest it counts to':>22} "
      f"{'words up to 8 it gets right':>29} {'out of':>8}")
for limit in range(1, 5):
    m = machine_for_depth(limit)
    right = sum(1 for w in words if m.accepts(w) == balanced(w))
    print(f"{limit + 1:>8} {limit:>22} {right:>29} {len(words):>8}")
print()
m = machine_for_depth(2)
deep = [w for w in words if balanced(w) and not m.accepts(w)]
print(f"balanced words up to length 8 the 3-state machine rejects: {len(deep)}")
print(f"the shortest of them: {min(deep, key=len)}")
