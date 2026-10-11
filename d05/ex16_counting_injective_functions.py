"""Counting the functions that never repeat an output."""
from dmkit.counting import enumerate_check, functions_from, report_count
from dmkit.sets import is_injective


def falling(n, k):
    """The product n * (n-1) * ... with k factors: the count of injective functions."""
    result = 1
    for i in range(k):
        result *= n - i
    return result


print(f"{'domain':>8} {'codomain':>10} {'by the rule':>13} {'by building':>13} "
      f"{'agree':>7}")
for domain in range(0, 5):
    for codomain in range(1, 5):
        dom = list(range(domain))
        cod = list("abcd"[:codomain])
        counted = falling(codomain, domain)
        result = enumerate_check(
            counted,
            lambda d=dom, c=cod: [f for f in functions_from(d, c) if is_injective(f)],
            "")
        print(f"{domain:>8} {codomain:>10} {counted:>13} {result['built']:>13} "
              f"{str(result['agree']):>7}")
