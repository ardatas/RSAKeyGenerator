# RSA Key Generator

## About
This is an educational project to generate RSA keys of size 2048 bit.

## Functions

### RSA (`rsa.py`)
| Function | Description |
|----------|-------------|
| `generate_keypair()` | Generates RSA public/private key pair (e,n) and (d,n) |

### MathUtils (`math_utils.py`)
| Function | Description |
|----------|-------------|
| `gcd(a, b)` | Computes greatest common divisor using Euclidean algorithm |
| `extended_gcd(a, b)` | Returns GCD along with Bézout coefficients |
| `mod_inverse(a, m)` | Computes modular multiplicative inverse |
| `mod_exp(base, exp, mod)` | Performs modular exponentiation via square-and-multiply |

### PrimeUtils (`prime_utils.py`)
| Function | Description |
|----------|-------------|
| `fermat_test(a, p)` | Fermat primality test for candidate `p` |
| `generate_prime(bit_len)` | Generates a random prime of specified bit length |
| `MillerRabin(n, k)` | Miller-Rabin probabilistic primality test with `k` rounds | 