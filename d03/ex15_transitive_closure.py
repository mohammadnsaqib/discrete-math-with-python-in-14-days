"""Adding every two-step route until nothing new appears."""
from dmkit.sets import is_transitive, transitive_closure

step = {(1, 2), (2, 3), (3, 4), (4, 5)}
print(f"the relation      : {sorted(step)}")
print(f"transitive?       : {is_transitive(step)}")
print()
current = set(step)
round_number = 0
while True:
    round_number += 1
    new = {(x, w) for x, y in current for z, w in current if y == z}
    added = new - current
    if not added:
        print(f"round {round_number}: nothing new, so it stops")
        break
    print(f"round {round_number}: adds {sorted(added)}")
    current |= new
closure = transitive_closure(step)
print()
print(f"the closure       : {sorted(closure)}")
print(f"pairs             : {len(step)} became {len(closure)}")
print(f"transitive now?   : {is_transitive(closure)}")
