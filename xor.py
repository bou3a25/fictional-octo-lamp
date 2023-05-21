def xor_encrypt_decrypt(message, key):
    encrypted = []
    for char in message:
        encrypted_char = chr(ord(char) ^ key)
        encrypted.append(encrypted_char)
    return ''.join(encrypted)


def xor_encrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as file_in, open(output_file, 'wb') as file_out:
        key_length = len(key)
        key_index = 0

        while True:
            byte = file_in.read(1)
            if not byte:
                break

            encrypted_byte = bytes([byte[0] ^ key[key_index]])
            file_out.write(encrypted_byte)

            key_index = (key_index + 1) % key_length


def xor_decrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as file_in, open(output_file, 'wb') as file_out:
        key_length = len(key)
        key_index = 0

        while True:
            byte = file_in.read(1)
            if not byte:
                break

            decrypted_byte = bytes([byte[0] ^ key[key_index]])
            file_out.write(decrypted_byte)

            key_index = (key_index + 1) % key_length




if __name__ == "__main__":
    # Example usage
    original_string = "Hello, World!"
    encryption_key = 42  # Secret key

    encrypted_string = xor_encrypt_decrypt(original_string, encryption_key)
    print("Encrypted String:", encrypted_string)

    decrypted_string = xor_encrypt_decrypt(encrypted_string, encryption_key)
    print("Decrypted String:", decrypted_string)

    ##############
    input_file = 'plaintext.txt'  # Replace with the path to your input file
    output_file = 'encrypted.txt'  # Replace with the desired output file path
    key = b'MySecretKey'  # Replace with your own encryption key

    xor_encrypt_file(input_file, output_file, key)


    encrypted_file = 'encrypted.txt'  # Replace with the path to your encrypted file
    decrypted_file = 'decrypted.txt'  # Replace with the desired decrypted file path
    key = b'MySecretKey'  # Replace with your encryption key

    xor_decrypt_file(encrypted_file, decrypted_file, key)
