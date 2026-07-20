# RSA Encryption and Decryption (CLI)
from math import gcd
# Calculate modular inverse
def mod_inverse(e, phi):
    for d in range(2, phi):
        if (d * e) % phi == 1:
            return d
    return None
# Encrypt message
def encrypt(message, e, n):
    encrypted = []
    for ch in message:
        encrypted.append(pow(ord(ch), e, n))
    return encrypted
# Decrypt message
def decrypt(cipher, d, n):
    text = ""
    for num in cipher:
        text += chr(pow(num, d, n))
    return text
print("RSA Encryption")
p = int(input("Enter first prime number (p): "))
q = int(input("Enter second prime number (q): "))
n = p * q
phi = (p - 1) * (q - 1)
print("\nValue of n =", n)
print("Value of φ(n) =", phi)
while True:
    e = int(input("\nEnter value of e: "))
    if gcd(e, phi) == 1:
        break
    else:
        print("e must be coprime with φ(n). Try again.")
d = mod_inverse(e, phi)
print("\nPublic Key :", (e, n))
print("Private Key:", (d, n))
message = input("\nEnter Message : ")
cipher = encrypt(message, e, n)
print("\nEncrypted Message:")
print(cipher)
plain = decrypt(cipher, d, n)
print("\nDecrypted Message:")
print(plain)
