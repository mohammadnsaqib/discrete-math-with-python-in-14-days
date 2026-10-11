"""How many functions run between two finite sets, counted and then built."""
from dmkit.counting import (count_functions, enumerate_check, functions_from,
                            report_count)

print(f"{'domain':>8} {'codomain':>10} {'by the rule':>13} {'by building':>13} "
      f"{'agree':>7}")
for domain in range(0, 5):
    for codomain in range(1, 4):
        dom = list(range(domain))
        cod = list("abc"[:codomain])
        counted = count_functions(domain, codomain)
        result = enumerate_check(counted, lambda d=dom, c=cod: functions_from(d, c), "")
        print(f"{domain:>8} {codomain:>10} {counted:>13} {result['built']:>13} "
              f"{str(result['agree']):>7}")
print()
print("the four functions from a two-member domain into a two-member codomain:")
for f in functions_from([0, 1], ["a", "b"]):
    print(f"   {f}")
