
from math_utils import MathUtils
from prime_utils import PrimeUtils

class RSA:

    @staticmethod
    def generate_keypair():

        # Use a smaller modulus for faster demo key generation.
        # This is NOT secure for real-world use but keeps the UI responsive.
        bit_len = 1024
        e = 65537           # common choice

        p = PrimeUtils.generate_prime(bit_len)
        q = PrimeUtils.generate_prime(bit_len)

        if p == q:
            while p == q:
                q = PrimeUtils.generate_prime(bit_len)


        n = p * q
        phiN = (p - 1) * (q - 1)      # ϕ(n)=(p−1)⋅(q−1)

        d = MathUtils.mod_inverse(e, phiN)  # d is the multiplicative inverse of e modulo φ(n)`
        return (e,n), (d,n)
