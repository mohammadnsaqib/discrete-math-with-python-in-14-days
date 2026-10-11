"""A function is a relation with one rule added: each input appears exactly once."""
from dmkit.sets import is_function

dom = {1, 2, 3}
candidates = [
    ("f: every input once", [(1, "a"), (2, "b"), (3, "a")]),
    ("an input used twice", [(1, "a"), (1, "b"), (2, "c"), (3, "a")]),
    ("an input missing", [(1, "a"), (2, "b")]),
    ("nothing at all", []),
    ("all three to one output", [(1, "a"), (2, "a"), (3, "a")]),
]
print(f"{'pairs':>26} {'a function on {1,2,3}?':>24}")
for name, pairs in candidates:
    print(f"{name:>26} {str(is_function(pairs, dom)):>24}")
