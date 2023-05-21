from Crypto.PublicKey import RSA

def load_key_from_file(filename):
    with open(filename, 'rb') as file:
        key_data = file.read()
        key = RSA.import_key(key_data)
    return key
if __name__ == "__main__":
    # Example usage:
    public_key_filename = 'public_key.pem'
    private_key_filename = 'private_key.pem'

    # Load the public key from file
    public_key = load_key_from_file(public_key_filename)
    print("Public key loaded:", public_key)

    # Load the private key from file
    private_key = load_key_from_file(private_key_filename)
    print("Private key loaded:", private_key)
