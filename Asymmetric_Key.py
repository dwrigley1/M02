from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# generate a public key for all to see, then a private one to decrypt later
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# private key for decryption 
with open("Private_Key.pem", "wb") as f:
    f.write(
        private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),  # demo only
        )
    )
# public key for encryption
with open("Public_Key.pem", "wb") as f:
    f.write(
        public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        )
    )

# get user input, encrypt it via public key
encrypted_message = input("Your Encrypted Message Is -> ").encode("utf-8")
ciphertext = public_key.encrypt(
    encrypted_message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    ),
)

# save as a binary file
with open("Cipher_Text.bin", "wb") as f:
    f.write(ciphertext)

print("Asymmetric Process Has Been Completed!") # used to ensure all lines have been parsed correctly
