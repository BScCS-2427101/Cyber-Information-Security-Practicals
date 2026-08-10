import hashlib
import math
# Function to check whether a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Extended Euclidean Algorithm
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

# Calculate modular inverse
def modular_inverse(e, phi):
    gcd, x, y = extended_gcd(e, phi)
    if gcd != 1:
        return None
    return x % phi

# Generate SHA-256 hash
def generate_hash(message):
    hash_value = hashlib.sha256(message.encode()).hexdigest()
    return hash_value

# Convert hexadecimal hash into integer
def hash_to_integer(hash_value):
    return int(hash_value, 16)

# Generate RSA keys
def generate_rsa_keys(p, q, e):
    n = p * q
    phi = (p - 1) * (q - 1)
    if math.gcd(e, phi) != 1:
        return None
    d = modular_inverse(e, phi)
    return n, phi, d

# Create digital signature
def create_signature(message, d, n):
    hash_value = generate_hash(message)
    hash_integer = hash_to_integer(hash_value)

    # RSA signature
    signature = pow(hash_integer, d, n)
    return hash_value, signature

# Verify digital signature
def verify_signature(message, signature, e, n):
    hash_value = generate_hash(message)
    hash_integer = hash_to_integer(hash_value)

    # Recover hash from signature
    recovered_hash = pow(signature, e, n)
    # Since small educational RSA keys may not contain the
    # complete SHA-256 integer, compare modulo n.
    if recovered_hash == hash_integer % n:
        return True, hash_value, recovered_hash
    else:
        return False, hash_value, recovered_hash
    
# ---------------- MAIN PROGRAM ----------------
print("=" * 60)
print("       RSA DIGITAL SIGNATURE IMPLEMENTATION")
print("=" * 60)
# Input prime numbers
while True:
    p = int(input("\nEnter first prime number (p): "))
    if is_prime(p):
        break
    else:
        print("Error: p must be a prime number.")
while True:
    q = int(input("Enter second prime number (q): "))
    if is_prime(q) and q != p:
        break
    else:
        print("Error: q must be a different prime number.")

# Calculate n and phi
n = p * q
phi = (p - 1) * (q - 1)
print("\nCalculated RSA values:")
print("n =", n)
print("phi(n) =", phi)

# Select public exponent
while True:
    e = int(input("\nEnter public exponent (e): "))
    if 1 < e < phi and math.gcd(e, phi) == 1:
        break
    else:
        print("Invalid e. It must satisfy gcd(e, phi) = 1.")

# Calculate private key
d = modular_inverse(e, phi)
print("\nRSA Keys:")
print("Public Key  =", (e, n))
print("Private Key =", (d, n))

# Input original message
message = input("\nEnter message to digitally sign: ")

# Generate digital signature
original_hash, signature = create_signature(message, d, n)
print("\n" + "=" * 60)
print("DIGITAL SIGNATURE GENERATION")
print("=" * 60)
print("Original Message :", message)
print("SHA-256 Hash     :", original_hash)
print("Digital Signature:", signature)


# Verification message
verification_message = input(
    "\nEnter message for signature verification: "
)
valid, received_hash, recovered_hash = verify_signature(
    verification_message,
    signature,
    e,
    n
)

print("\n" + "=" * 60)
print("DIGITAL SIGNATURE VERIFICATION")
print("=" * 60)
print("Received Message :", verification_message)
print("SHA-256 Hash     :", received_hash)
print("Recovered Hash   :", recovered_hash)

if valid:
    print("\nResult: DIGITAL SIGNATURE VERIFIED")
    print("The message is authentic and its integrity is maintained.")
else:
    print("\nResult: DIGITAL SIGNATURE VERIFICATION FAILED")
    print("The message may have been modified or the signature is invalid.")

print("\n" + "=" * 60)
print("END OF PRACTICAL")
print("=" * 60)
