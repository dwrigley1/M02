from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

# load the private key for decryption
with open("Private_Key.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(f.read(), password=None) # password positional argument is required

# now we can read the file since the key is decrypted
with open("Cipher_Text.bin", "rb") as f:
    ciphertext = f.read()

# this portion is what actually decrypts the key
plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    ),
)

print("Your Decrypted Message Is -> ", plaintext.decode("utf-8"))
