#Design and implement algorithms to encrypt and decrypt messages using transposition techniques.
def encrypt(text):
    first = ""
    second = ""
    for i in range(len(text)):
        if i % 2 == 0:
            first += text[i]
        else:
            second += text[i]
    return first + second
def decrypt(text):
    mid = (len(text) + 1) // 2
    first = text[:mid]
    second = text[mid:]
    result = ""
    for i in range(mid):
        result += first[i]
        if i < len(second):
            result += second[i]
    return result
message = input("Enter message: ")
encrypted = encrypt(message)
print("\nEncrypted Message :", encrypted)
decrypted = decrypt(encrypted)
print("Decrypted Message :", decrypted)
