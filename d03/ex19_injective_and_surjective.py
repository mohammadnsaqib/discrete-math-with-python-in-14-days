"""Injective and surjective, and why only two of the four combinations exist here."""
from dmkit.sets import is_bijective, is_injective, is_surjective

dom = {1, 2, 3}
codomain = {"a", "b", "c"}
# Only two rows are possible here, and the reason is the lesson. On a domain and
# codomain of the same finite size, injective and surjective are the same condition, so
# "injective but not surjective" cannot be built at all.
functions = [
    ("both", [(1, "a"), (2, "b"), (3, "c")]),
    ("neither", [(1, "a"), (2, "a"), (3, "a")]),
]
print(f"{'function':>30} {'injective':>11} {'surjective':>12} {'bijective':>11}")
for name, pairs in functions:
    print(f"{str(pairs):>30} {str(is_injective(pairs)):>11} "
          f"{str(is_surjective(pairs, codomain)):>12} "
          f"{str(is_bijective(pairs, dom, codomain)):>11}")
print()
bigger = {"a", "b", "c", "d"}
small = [(1, "a"), (2, "b"), (3, "c")]
print("the same three pairs, into a codomain of four:")
print(f"   injective  : {is_injective(small)}")
print(f"   surjective : {is_surjective(small, bigger)}")
