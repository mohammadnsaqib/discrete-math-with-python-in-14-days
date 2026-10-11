"""How many functions there are, counted by building every one of them."""
from itertools import product

from dmkit.sets import is_bijective, is_injective, is_surjective

print(f"{'domain':>8} {'codomain':>10} {'all':>8} {'injective':>11} {'surjective':>12} "
      f"{'bijective':>11}")
for n in (1, 2, 3):
    for m in (1, 2, 3):
        dom = list(range(1, n + 1))
        cod = list("abc"[:m])
        every = [list(zip(dom, outs)) for outs in product(cod, repeat=n)]
        inj = sum(1 for f in every if is_injective(f))
        sur = sum(1 for f in every if is_surjective(f, cod))
        bij = sum(1 for f in every if is_bijective(f, dom, cod))
        print(f"{n:>8} {m:>10} {len(every):>8} {inj:>11} {sur:>12} {bij:>11}")
