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
            if MillerRabin(p):
                return p


