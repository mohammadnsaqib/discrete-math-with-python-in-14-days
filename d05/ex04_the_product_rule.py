"""The product rule, and the collection it claims to size."""
from itertools import product

from dmkit.counting import enumerate_check, product_rule, report_count

sizes = ["small", "large"]
flavours = ["plain", "salted", "sweet"]
boxes = ["paper", "tin"]

print(f"{'collection':>34} {'by the rule':>12} {'by building':>12}  verdict")
print(report_count(enumerate_check(
    product_rule(len(sizes), len(flavours)),
    lambda: list(product(sizes, flavours)),
    "a size and a flavour")))
print(report_count(enumerate_check(
    product_rule(len(sizes), len(flavours), len(boxes)),
    lambda: list(product(sizes, flavours, boxes)),
    "a size, a flavour and a box")))
print(report_count(enumerate_check(
    product_rule(len(sizes), 0),
    lambda: list(product(sizes, [])),
    "a size and one of nothing")))
print()
print("the first four of the twelve:")
for combination in list(product(sizes, flavours, boxes))[:4]:
    print(f"   {combination}")
