"""One exchange from key to message and back, on a key large enough to be slow to break.
"""
from dmkit.crypto import rsa_decrypt, rsa_encrypt, rsa_keys, totient
from dmkit.induct import best_of
from dmkit.number import factorise, is_prime_trial

p, q = 1000003, 1000033
keys = rsa_keys(p, q, e=65537)
n, e = keys["public"]
_, d = keys["private"]
phi = keys["phi"]
message = 20260910
cipher = rsa_encrypt(message, keys["public"])
back = rsa_decrypt(cipher, keys["private"])

print(f"two primes: {p} and {q}, both prime: "
      f"{is_prime_trial(p) and is_prime_trial(q)}")
print(f"the modulus  : {n}, which has {len(str(n))} digits")
print(f"the totient  : {phi}, and totient() agrees: {totient(n) == phi}")
print(f"the exponents: {e} and {d}, with e * d modulo the totient {e * d % phi}")
print()
print(f"{'message':>12} {'encrypted':>18} {'decrypted':>12} {'returned':>10}")
print(f"{message:>12} {cipher:>18} {back:>12} {str(back == message):>10}")
sample = [1, 2, 999999, 12345678, n - 1]
failures = [m for m in sample
            if rsa_decrypt(rsa_encrypt(m, keys["public"]), keys["private"]) != m]
print(f"messages tried: {sample}, and those that did not come back: {failures}")
print()
print(f"{'step':>28} {'seconds':>12}")
for name, work in (("encrypting", lambda: rsa_encrypt(message, keys["public"])),
                   ("decrypting", lambda: rsa_decrypt(cipher, keys["private"])),
                   ("factoring the modulus", lambda: factorise(n))):
    print(f"{name:>28} {best_of(work, 3):>12.6f}")
