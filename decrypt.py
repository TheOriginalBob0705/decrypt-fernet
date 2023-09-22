from cryptography.fernet import Fernet

with open("key.txt","rb") as f:
    key = f.read()
f = Fernet(key)

with open('encrypted_file.txt', 'rb') as encrypted_file:
    encrypted = encrypted_file.read()

decrypted = f.decrypt(encrypted)

with open('decrypted_file.txt', 'wb') as decrypted_file:
    decrypted_file.write(decrypted)
