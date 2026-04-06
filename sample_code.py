from Crypto.PublicKey import RSA
from Crypto.Cipher import AES

# This is a vulnerable legacy implementation
key = RSA.generate(2048) 
cipher = AES.new(b'sixteen_byte_key', AES.MODE_CBC)

print("Encrypted with RSA-2048 and AES-CBC")
