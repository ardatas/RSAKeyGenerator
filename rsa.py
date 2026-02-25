
from math_utils import MathUtils
from prime_utils import PrimeUtils

class RSA:

    @staticmethod
    def generate_keypair():

        bit_len = 2048
        e = 64473           # common choice

        p = PrimeUtils.generate_prime(bit_len)
        q = PrimeUtils.generate_prime(bit_len)

        if p == q:
            while p == q:
                q = PrimeUtils.generate_prime(bit_len)


        n = p * q
        phiN = (p - 1) * (q - 1)      # ϕ(n)=(p−1)⋅(q−1)

        d = MathUtils.extended_gcd(e, phiN)  # d is the multiplicative inverse of e modulo φ(n)`
        return (e,n), (d,n)


print(RSA.generate_keypair())
