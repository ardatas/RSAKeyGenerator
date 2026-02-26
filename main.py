from rsa import RSA

def main():
    print("Generating 2048-bit RSA keypair...\n")
    public_key, private_key = RSA.generate_keypair()

    e, n = public_key
    d, _ = private_key

    print(f"Public key (e):  {e}")
    print(f"Private key (d): {d}")
    print(f"Modulus (n):     {n}")
    print(f"\nKey size: {n.bit_length()} bits")

    # Quick encrypt/decrypt test with a small message
    message = "hello my name is arda"
    ciphertext = pow(message, e, n)
    decrypted = pow(ciphertext, d, n)

    print(f"\n--- Encrypt / Decrypt Test ---")
    print(f"Original message:  {message}")
    print(f"Encrypted:         {ciphertext}")
    print(f"Decrypted:         {decrypted}")
    print(f"Round-trip OK:     {decrypted == message}")

if __name__ == "__main__":
    main()
