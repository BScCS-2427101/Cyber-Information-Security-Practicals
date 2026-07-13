#To design and implement an algorithm to encrypt and decrypt messages using the Classical Substitution Technique (Caesar Cipher).
def encrypt(text, shift):
    result = ""
    for ch in text:
        if ch.isalpha():
            if ch.isupper():
                result += chr((ord(ch) - 65 + shift) % 26 + 65)
            else:
                result += chr((ord(ch) - 97 + shift) % 26 + 97)
        else:
            result += ch
    return result
def decrypt(text, shift):
    return encrypt(text, -shift)
message = input("Enter Message : ")
shift = int(input("Enter Shift Value : "))
encrypted = encrypt(message, shift)
print("Encrypted Message :", encrypted)
decrypted = decrypt(encrypted, shift)
print("Decrypted Message :", decrypted)
