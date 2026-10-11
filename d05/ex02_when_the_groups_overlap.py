"""What the sum rule reports when its one condition is not met."""
from dmkit.counting import enumerate_check, report_count, sum_rule

under_20 = list(range(1, 20))
evens = [n for n in under_20 if n % 2 == 0]
multiples_of_3 = [n for n in under_20 if n % 3 == 0]
shared = sorted(set(evens) & set(multiples_of_3))

print(f"evens under 20          : {evens}")
print(f"multiples of 3 under 20 : {multiples_of_3}")
print(f"in both                 : {shared}")
print()
print(f"{'collection':>34} {'by the rule':>12} {'by building':>12}  verdict")
print(report_count(enumerate_check(
    sum_rule(len(evens), len(multiples_of_3)),
    lambda: sorted(set(evens) | set(multiples_of_3)),
    "even or a multiple of 3")))
print(report_count(enumerate_check(
    sum_rule(len(evens), len(multiples_of_3)) - len(shared),
    lambda: sorted(set(evens) | set(multiples_of_3)),
    "the same, with the overlap removed")))
print()
print(f"the sum rule overcounts by {len(shared)}, which is the size of the overlap.")
print("Its one condition, that no member is in both groups, was not met.")
