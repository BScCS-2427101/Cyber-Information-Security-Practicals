import math
# Function to check whether a number is prime
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

# ---------------- MAIN PROGRAM ----------------
print("=" * 60)
print("       DIFFIE-HELLMAN KEY EXCHANGE")
print("=" * 60)
print("\nPublic parameters are shared between User 1 and User 2.")
print("Private keys must remain secret.\n")

# ---------------- INPUT p ----------------
while True:
    try:
        p = int(input("Enter a prime number (p): "))

        if is_prime(p):
            break
        else:
            print("Error: p must be a prime number.")
    except ValueError:
        print("Error: Please enter a valid integer.")

# ---------------- INPUT g ----------------
while True:
    try:
        g = int(input("Enter generator (g): "))
        if 1 < g < p:
            break
        else:
            print("Error: g must satisfy 1 < g < p.")
    except ValueError:
        print("Error: Please enter a valid integer.")

# ---------------- USER 1 PRIVATE KEY ----------------
while True:
    try:
        user1_private = int(
            input("\nEnter User 1 private key: ")
        )
        if user1_private > 0:
            break
        else:
            print("Private key must be greater than 0.")
    except ValueError:
        print("Error: Please enter a valid integer.")

# ---------------- USER 2 PRIVATE KEY ----------------
while True:
    try:
        user2_private = int(
            input("Enter User 2 private key: ")
        )
        if user2_private > 0:
            break
        else:
            print("Private key must be greater than 0.")
    except ValueError:
        print("Error: Please enter a valid integer.")

# ---------------- PUBLIC KEY CALCULATION ----------------
user1_public = pow(
    g,
    user1_private,
    p
)
user2_public = pow(
    g,
    user2_private,
    p
)

# ---------------- DISPLAY PUBLIC INFORMATION ----------------
print("\n" + "=" * 60)
print("PUBLIC PARAMETERS")
print("=" * 60)
print("Prime number (p):", p)
print("Generator (g)  :", g)


# ---------------- DISPLAY PUBLIC KEYS ----------------
print("\n" + "=" * 60)
print("PUBLIC KEY GENERATION")
print("=" * 60)
print("User 1 Public Key:", user1_public)
print("User 2 Public Key:", user2_public)


# ---------------- SHARED SECRET CALCULATION ----------------
user1_shared_secret = pow(
    user2_public,
    user1_private,
    p
)
user2_shared_secret = pow(
    user1_public,
    user2_private,
    p
)

# ---------------- DISPLAY SHARED KEYS ----------------
print("\n" + "=" * 60)
print("SHARED SECRET KEY CALCULATION")
print("=" * 60)
print("User 1 calculates:")
print(
    "Shared Key = User 2 Public Key ^ User 1 Private Key mod p"
)
print(
    "User 1 Shared Secret Key:",
    user1_shared_secret
)
print("\nUser 2 calculates:")
print(
    "Shared Key = User 1 Public Key ^ User 2 Private Key mod p"
)
print(
    "User 2 Shared Secret Key:",
    user2_shared_secret
)

# ---------------- VERIFICATION ----------------
print("\n" + "=" * 60)
print("KEY VERIFICATION")
print("=" * 60)
if user1_shared_secret == user2_shared_secret:
    print(
        "User 1 Shared Key:",
        user1_shared_secret
    )
    print(
        "User 2 Shared Key:",
        user2_shared_secret
    )
    print("\nSUCCESS!")
    print(
        "Both users generated the same shared secret key."
    )
    print(
        "The Diffie-Hellman key exchange was successful."
    )
else:
    print(
        "User 1 Shared Key:",
        user1_shared_secret
    )
    print(
        "User 2 Shared Key:",
        user2_shared_secret
    )
    print("\nFAILED!")
    print(
        "The shared keys are different."
    )
print("\n" + "=" * 60)
print("END OF PRACTICAL")
print("=" * 60)
