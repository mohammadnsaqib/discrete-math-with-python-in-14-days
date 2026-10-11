"""What an attacker has to do, and how long it takes when the key is small."""
from dmkit.crypto import mod_inverse, rsa_decrypt, rsa_encrypt, rsa_keys
from dmkit.induct import best_of
from dmkit.number import factorise


def break_key(public):
    """Recover the private exponent from the public key alone, by factoring."""
    n, e = public
    factors = factorise(n)
    if len(factors) != 2 or any(power != 1 for _, power in factors):
        raise ValueError("this key is not a product of two distinct primes")
    p, q = factors[0][0], factors[1][0]
    return mod_inverse(e, (p - 1) * (q - 1)), (p, q)


keys = rsa_keys(61, 53, e=17)
public, private = keys["public"], keys["private"]
recovered, primes = break_key(public)
cipher = rsa_encrypt(2790, public)
print(f"the public key alone : {public}")
print(f"factoring the modulus: {primes}, giving the private exponent {recovered}")
print(f"the real one is {private[1]}, and they match: {recovered == private[1]}")
print(f"a message of 2790 encrypts to {cipher} and the recovered exponent returns "
      f"{rsa_decrypt(cipher, (public[0], recovered))}")
print()
print(f"{'primes':>18} {'modulus':>16} {'digits':>8} {'seconds to break':>18}")
for p, q in ((61, 53), (1009, 1013), (10007, 10009), (100003, 100019)):
    keys = rsa_keys(p, q)
    seconds = best_of(lambda k=keys["public"]: break_key(k), 3)
    print(f"{f'{p}, {q}':>18} {keys['public'][0]:>16} "
          f"{len(str(keys['public'][0])):>8} {seconds:>18.6f}")
