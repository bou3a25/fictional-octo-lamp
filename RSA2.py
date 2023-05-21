from datetime import datetime, timedelta
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

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
    duration = 3600  # 1 hour (you can set the desired duration in seconds)
    return key_pair, created_time, duration

def encrypt_file(input_file, output_file, public_key):
    cipher = PKCS1_OAEP.new(public_key)
    with open(input_file, 'rb') as file_in, open(output_file, 'wb') as file_out:
        while True:
            chunk = file_in.read(128)
            if len(chunk) == 0:
                break
            encrypted_chunk = cipher.encrypt(chunk)
            file_out.write(encrypted_chunk)

def decrypt_file(input_file, output_file, private_key):
    cipher = PKCS1_OAEP.new(private_key)
    with open(input_file, 'rb') as file_in, open(output_file, 'wb') as file_out:
        while True:
            chunk = file_in.read(256)
            if len(chunk) == 0:
                break
            decrypted_chunk = cipher.decrypt(chunk)
            file_out.write(decrypted_chunk)
if __name__ == "__main__":
    # Generate the initial key pair
    current_key_pair, current_created_time, current_duration = generate_new_key_pair()

    # Example usage:
    input_filename = 'input.txt'
    encrypted_filename = 'encrypted.bin'
    decrypted_filename = 'decrypted.txt'

    # Encrypt the file
    encrypt_file(input_filename, encrypted_filename, current_key_pair.publickey())
    print("File encrypted:", encrypted_filename)

    # Simulate time passing
    # current_created_time += timedelta(hours=1)  # Add 1 hour to the current created time

    # Check if the key has expired
    if is_key_expired(current_created_time, current_duration):
        # Generate a new key pair
        current_key_pair, current_created_time, current_duration = generate_new_key_pair()

    # Decrypt the file
    decrypt_file(encrypted_filename, decrypted_filename, current_key_pair)
    print("File decrypted:", decrypted_filename)
