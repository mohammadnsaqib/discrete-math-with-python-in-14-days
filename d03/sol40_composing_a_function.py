"""Problem 3.27: composing functions, and the properties that survive it."""
from dmkit.sets import compose, is_bijective, is_injective, is_surjective

dom = [1, 2, 3]
mid = ["a", "b", "c"]
end = ["x", "y", "z"]

f = [(1, "a"), (2, "b"), (3, "c")]           # bijective
g = [("a", "x"), ("b", "x"), ("c", "y")]     # neither
h = [("a", "x"), ("b", "y"), ("c", "z")]     # bijective

for name, first, second, first_cod, second_cod in (
        ("f then g", f, g, mid, end), ("f then h", f, h, mid, end)):
    composed = compose(first, second)
    print(f"{name}")
    print(f"   first  : injective {is_injective(first)}, "
          f"surjective {is_surjective(first, first_cod)}")
    print(f"   second : injective {is_injective(second)}, "
          f"surjective {is_surjective(second, second_cod)}")
    print(f"   result : {composed}")
    print(f"            injective {is_injective(composed)}, "
          f"surjective {is_surjective(composed, second_cod)}")
    print()
