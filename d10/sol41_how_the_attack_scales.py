"""Problem 10.28: the cost of using a key against the cost of breaking it."""
from dmkit.crypto import mod_inverse, rsa_decrypt, rsa_encrypt, rsa_keys
from dmkit.induct import best_of
from dmkit.number import factorise, sieve


def break_key(public):
    """Recover the private exponent from the public key by factoring the modulus."""
    n, e = public
    factors = factorise(n)
    p, q = factors[0][0], factors[-1][0]
    return mod_inverse(e, (p - 1) * (q - 1))


BATCH = 300
pairs = [(101, 103), (1009, 1013), (10007, 10009), (100003, 100019),
         (1000003, 1000033)]
print(f"{'primes':>22} {'modulus':>16} {'digits':>8} {'encrypt':>11} "
      f"{'decrypt':>11} {'break':>12} {'break / decrypt':>17}")
for p, q in pairs:
    keys = rsa_keys(p, q, e=65537 if (p - 1) * (q - 1) > 65537 else None)
    public, private = keys["public"], keys["private"]
    message = min(12345, public[0] - 1)
    cipher = rsa_encrypt(message, public)
    # THE TWO FAST STEPS ARE TIMED IN BATCHES. One call runs in a few microseconds,
    # which is close enough to the clock's resolution that a single measurement is
    # mostly noise.
    encrypt = best_of(lambda: [rsa_encrypt(message, public)
                               for _ in range(BATCH)], 3) / BATCH
    decrypt = best_of(lambda: [rsa_decrypt(cipher, private)
                               for _ in range(BATCH)], 3) / BATCH
    attack = best_of(lambda k=public: break_key(k), 3)
    recovered = break_key(public)
    assert recovered == private[1]
    print(f"{f'{p}, {q}':>22} {public[0]:>16} {len(str(public[0])):>8} "
          f"{encrypt:>11.8f} {decrypt:>11.8f} {attack:>12.6f} "
          f"{attack / decrypt:>17.1f}")
print()
print(f"{'digits in the modulus':>24} {'candidates to try':>20}")
for digits in (12, 16, 20, 40, 100, 617):
    print(f"{digits:>24} {f'about 10**{digits // 2}':>20}")
