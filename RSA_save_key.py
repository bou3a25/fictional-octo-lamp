from Crypto.PublicKey import RSA

def generate_rsa_key_pair():
    key = RSA.generate(2048)
    return key

def save_key_to_file(key, filename):
    with open(filename, 'wb') as file:
        file.write(key.export_key('PEM'))
if __name__ == "__main__":
    # Generate the key pair
    key_pair = generate_rsa_key_pair()

    # Save the public key to a file
    public_key_filename = 'public_key.pem'
    save_key_to_file(key_pair.publickey(), public_key_filename)
    print("Public key saved to:", public_key_filename)

    # Save the private key to a file
    private_key_filename = 'private_key.pem'
    save_key_to_file(key_pair, private_key_filename)
    print("Private key saved to:", private_key_filename)
