from datetime import datetime, timedelta
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from time import sleep
def generate_rsa_key_pair():
    key = RSA.generate(2048)
    return key

def is_key_expired(created_time, duration):
    current_time = datetime.now()
    expiration_time = created_time + timedelta(seconds=duration)
    return current_time >= expiration_time

def generate_new_key_pair():
    key_pair = generate_rsa_key_pair()
    created_time = datetime.now()
    duration = 5  # 1 hour (you can set the desired duration in seconds)
    return key_pair, created_time, duration

def encrypt_message(message, public_key):
    cipher = PKCS1_OAEP.new(public_key)
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message

def decrypt_message(ciphertext, private_key):
    cipher = PKCS1_OAEP.new(private_key)
    decrypted_message = cipher.decrypt(ciphertext)
    return decrypted_message.decode()

if __name__ == "__main__":
    # Generate the initial key pair
    current_key_pair, current_created_time, current_duration = generate_new_key_pair()

    # Example usage:
    message = "Hello, world!"
    encrypted_msg = encrypt_message(message, current_key_pair.publickey())
    print("Encrypted message:", encrypted_msg)

    # Simulate time passing
    #current_created_time += timedelta(3601)  # Add 1 hour to the current created time
    sleep(4)
    # Check if the key has expired
    if is_key_expired(current_created_time, current_duration):
        print("Key expired, generating a new key pair")
        # Generate a new key pair
        current_key_pair, current_created_time, current_duration = generate_new_key_pair()
    # Decrypt the message
    try:
        decrypted_msg = decrypt_message(encrypted_msg, current_key_pair)
        print("Decrypted message:", decrypted_msg)
    except ValueError:
        print("ValueError: Incorrect decryption.")