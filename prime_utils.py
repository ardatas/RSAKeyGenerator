from math_utils import MathUtils
import secrets

class PrimeUtils:

    @staticmethod
    def fermat_test(a, p):
        if MathUtils.mod_exp(a, p) == 1:
            return True
        else:
            return False

    # RSA modulus of size 2048 bit
    @staticmethod
    def generate_prime(bit_len):

        while True:
            p = secrets.randbits(bit_len // 2) # integer division
            p += not(p & 1)
            if PrimeUtils.MillerRabin(p):
                return p

    @staticmethod
    def MillerRabin(n, k=40):
        if n == 2:
            return True
        if n < 2 or n % 2 == 0:
            return False

        # write n-1 as 2^r * d
        r, d = 0, n - 1
        while d % 2 == 0:
            r += 1
            d //= 2

        for _ in range(k):
            a = secrets.randbelow(n - 3) + 2  # 2 <= a <= n-2
            x = pow(a, d, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True



