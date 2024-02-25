from colorful import colorful
from greetings import greet
from fcc_ciphers import encrypt, decrypt

print(
    colorful(
        "red", "_____________________________________________________________________"
    )
)

print(f"{greet()}, Monica")

text = "mrttaqrhknsw ih puggrur"
custom_key = "happycoding"

encryption = encrypt(text, custom_key)
print(encryption)
decryption = decrypt(encryption, custom_key)
print(decryption)

print(f"\nEncrypted text: {text}")
print(f"Key: {custom_key}")
decryption = decrypt(text, custom_key)
print(f"\nDecrypted text: {decryption}\n")
