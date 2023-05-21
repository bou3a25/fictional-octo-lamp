from RSA2 import *
from RSA_load_key import *
encrypted_filename = 'encrypted.bin'
decrypted_filename = 'decrypted.txt'

# Example usage:
public_key_filename = 'public_key.pem'
private_key_filename = 'private_key.pem'
# Load the public key from file
public_key = load_key_from_file(public_key_filename)
print("Public key loaded:", public_key)
# Load the private key from file
private_key = load_key_from_file(private_key_filename)
print("Private key loaded:", private_key)
use=input("use this key ")
if (use==""):
    try:
        decrypt_file(encrypted_filename, decrypted_filename, private_key)
        print("File decrypted:", decrypted_filename)
    except ValueError:
        print("ValueError: Incorrect decryption.")