# URL https://cryptography.io/en/latest/fernet/

from cryptography.fernet import Fernet  # Fernet (symmetric encryption)

key = Fernet.generate_key() # method to generate the secret key

f = Fernet(key) # assignment creates an object

message = input("Enter a message to encrypt: ") # obtain user input
bites = message.encode("utf-8") # convert data type to bytes, this is a requirement for Fernet
print("") # print space for readability

print(bites) # output has a 'b' in front to show it has been converted
print("") # print space for readability

token = f.encrypt(bites) # encrypt the message

print(token) # print the encryption key to the console
print("") # print space for readability

d = f.decrypt(token) # decrypt the message

print("The encrypted message was -> ",d.decode()) # print the decoded message in plain text