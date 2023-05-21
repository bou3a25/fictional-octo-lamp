from xor import xor_encrypt_file

input_file = 'input.txt'  # Replace with the path to your input file
output_file = 'input2.txt'  # Replace with the desired output file path
key = b'MySecretKey'  # Replace with your own encryption key

xor_encrypt_file(input_file, output_file, key)


import RSA_encryption