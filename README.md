* * * Symmetric_Encryption.py * * *
this Python file shows the process of symmetric encryption
it imports the Fernet module to allow for the encryption
creates the encryption key
takes a user's input
converts the plain text into bytes
the token encrypts the newly converted message
decrypts said token
prints the message


* * * Asymmetric_Key.py * * *
    *  * Run This First BEFORE Asymmetric_Decrypt.py * * 
generates a public key for anyone to be able to encrypt a message
generates a private key only a specific user would have
takes a user's input, encrypts the text
the file is .pem (Privacy Enhanced Mail) because it is a base64-encoded text file whereas
(when I was trying to use a .txt file, it kept failing when attempting to take a user's input, write to a binary file, open it in another .py file, but also decrypt it. something was getting lost between the text -> bytes-> text -> bytes, etc conversion)
 saves the cipher text as a .bin (Binary) file
prints a message to the console aleting the user the process has finished

* * * Asymmetric_Decrypt.py * * *
loads the private key for decryption
reads the .bin file now that we have used the decryption key
decrypts the message
prints it to the console


* * * URLs used for resources * * *
https://cryptography.io/en/latest/fernet/
https://cryptography.io/en/latest/hazmat/primitives/asymmetric/#
https://docs.python.org/3/library/base64.html
https://en.wikipedia.org/wiki/Privacy-Enhanced_Mail#:~:text=Privacy%2DEnhanced%20Mail%20(PEM),the%20IETF%20in%20RFC%207468.
https://www.techtarget.com/whatis/definition/binary-file
