# T101 Practical 3
# Message Authentication Code (MAC) using HMAC-SHA256
# CLI Version
import hmac
import hashlib
def generate_mac(message, key):
    mac = hmac.new(
        key.encode(),
        message.encode(),
        hashlib.sha256
    ).hexdigest()
    return mac
print("=" * 50)
print("     MESSAGE AUTHENTICATION CODE (MAC)")
print("=" * 50)
message = input("Enter Message : ")
key = input("Enter Secret Key : ")
mac = generate_mac(message, key)
print("\nGenerated MAC:")
print(mac)
print("Verification")
received_message = input("Enter Received Message : ")
received_key = input("Enter Secret Key : ")
received_mac = input("Enter Received MAC : ")
new_mac = generate_mac(received_message, received_key)
if hmac.compare_digest(new_mac, received_mac):
    print("\nMessage Verified Successfully")
    print("Integrity Maintained")
    print("Sender is Authentic")
else:
    print("\nVerification Failed")
    print("Message has been Modified or Key is Incorrect")
