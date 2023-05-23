from RSA2 import *
from RSA_save_key import *
from time import sleep

# Example usage:
input_filename = 'input2.txt'
encrypted_filename = 'encrypted.bin'
decrypted_filename = 'decrypted.txt'

while True:
    
    print("generate_new_key_pair")
    current_key_pair= generate_rsa_key_pair()

    # Save the public key to a file
    public_key_filename = 'public_key.pem'
    save_key_to_file(current_key_pair.publickey(), public_key_filename)
    print("Public key saved to:", public_key_filename)

    # Save the private key to a file
    private_key_filename = 'private_key.pem'
    save_key_to_file(current_key_pair, private_key_filename)
    print("Private key saved to:", private_key_filename)

    # Encrypt the file
    encrypt_file(input_filename, encrypted_filename, current_key_pair.publickey())
    print("File encrypted:", encrypted_filename)
    sleep(120)
