import argparse
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
import base64

def decrypt_data(encrypted_data_base64, path_to_private_key, key_password):
    # Decode the base64 encoded data
    encrypted_data = base64.b64decode(encrypted_data_base64)

    # Load the private key
    with open(path_to_private_key, 'rb') as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=key_password.encode('utf-8') if key_password else None,
            backend=default_backend()
        )

    # Assuming RSA encryption was used with PKCS1v15 padding
    decrypted_data = private_key.decrypt(
        encrypted_data,
        padding.PKCS1v15()
    )

    return decrypted_data.decode('utf-8')

def main():
    parser = argparse.ArgumentParser(description="Decrypt base64-encoded data with a private key.")
    parser.add_argument("encrypted_data", help="Base64-encoded encrypted data")
    parser.add_argument("private_key_path", help="Path to the private key file")
    parser.add_argument("--key_password", help="Password for the private key (if encrypted)", default=None)

    args = parser.parse_args()

    decrypted_data = decrypt_data(args.encrypted_data, args.private_key_path, args.key_password)
    print(decrypted_data)

if __name__ == "__main__":
    main()