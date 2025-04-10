from cryptography.fernet import Fernet

with open("secret.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)

with open(".env", "rb") as file:
    original = file.read()

encrypted = fernet.encrypt(original)

with open(".env.enc", "wb") as encrypted_file:
    encrypted_file.write(encrypted)

print("✅ .env criptografado com sucesso!")
