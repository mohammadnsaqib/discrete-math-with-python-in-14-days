"""Problem 10.25: everything the chapter can say about one modulus."""
from dmkit.crypto import mod_inverse, order_of, totient, totient_by_counting
from dmkit.number import gcd, is_prime_trial


def report(m):
    """The structure of arithmetic modulo m, computed rather than looked up."""
    invertible = [a for a in range(1, m) if gcd(a, m) == 1]
    orders = sorted({order_of(a, m) for a in invertible})
    return {"m": m, "prime": is_prime_trial(m), "totient": totient(m),
            "invertible": len(invertible), "orders": orders,
            "checks": (totient(m) == totient_by_counting(m)
                       and len(invertible) == totient(m)
                       and all(a * mod_inverse(a, m) % m == 1 for a in invertible)
                       and all(totient(m) % k == 0 for k in orders))}


print(f"{'m':>5} {'prime':>7} {'totient':>9} {'invertible':>12} {'orders present':>24} "
      f"{'checks pass':>13}")
for m in (5, 7, 8, 9, 12, 13, 15, 16, 17, 21):
    r = report(m)
    print(f"{r['m']:>5} {str(r['prime']):>7} {r['totient']:>9} {r['invertible']:>12} "
          f"{str(r['orders']):>24} {str(r['checks']):>13}")
print()
failed = [m for m in range(2, 200) if not report(m)["checks"]]
print(f"moduli from 2 to 199 where any check failed: {len(failed)}")
