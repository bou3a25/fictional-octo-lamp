from xor import xor_decrypt_file
from file import read_file

import RSA_decryption

encrypted_file = 'decrypted.txt'  # Replace with the path to your encrypted file
decrypted_file = 'decrypted2.txt'  # Replace with the desired decrypted file path
key = b'MySecretKey'  # Replace with your encryption key

xor_decrypt_file(encrypted_file, decrypted_file, key)

print(read_file('decrypted2.txt'))