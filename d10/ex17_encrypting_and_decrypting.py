"""One message through the whole system, and every message through it."""
from dmkit.crypto import rsa_decrypt, rsa_encrypt, rsa_keys

keys = rsa_keys(61, 53, e=17)
public, private = keys["public"], keys["private"]
n, e = public
_, d = private

print(f"the public key  : ({n}, {e})")
print(f"the private key : ({n}, {d})")
print()
print(f"{'message':>10} {'encrypted':>12} {'decrypted':>12} {'returned':>10}")
for message in (0, 1, 2, 42, 65, 1000, 3232):
    cipher = rsa_encrypt(message, public)
    back = rsa_decrypt(cipher, private)
    print(f"{message:>10} {cipher:>12} {back:>12} {str(back == message):>10}")
print()
failures = [m for m in range(n) if rsa_decrypt(rsa_encrypt(m, public), private) != m]
print(f"messages below {n} that do not come back: {len(failures)}")
print()
fixed = [m for m in range(n) if rsa_encrypt(m, public) == m]
print(f"messages that encrypt to themselves: {len(fixed)}, the first few being "
      f"{fixed[:6]}")
print()
try:
    rsa_encrypt(n + 1, public)
except ValueError as problem:
    print(f"a message of {n + 1}: {problem}")
