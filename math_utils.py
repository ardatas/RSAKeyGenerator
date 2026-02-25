class MathUtils:

    @staticmethod
    def gcd(a: int, b:int) -> int:
        if a == 0:
            return b
        a, b = min(a, b), max(a, b)
        return MathUtils.gcd(b, a % b)


    # returns gcd, alpha, beta
    @staticmethod
    def extended_gcd(a, b):
        if a == 0:
            return (b, 1, 0)

        gcd, x1, y1 = MathUtils.extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return (gcd, x, y)


    @staticmethod
    def mod_inverse(a, m):
        gcd, x, y = MathUtils.extended_gcd(a, m)
        if (gcd != 1):
            raise ValueError('modular inverse does not exist');

        return x

    @staticmethod
    def mod_exp(base, exp, mod):
        num = base ** exp
        return num % mod


# Test
print(MathUtils.extended_gcd(45, 63))

