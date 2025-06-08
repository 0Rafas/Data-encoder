import base64


class RafasCrypt:
    def __init__(self, key):
        self.key = key
        self.internal_decrypt_key = "Ne&1Ta#Jn_me"
    
    def _transform_char(self, char_code, key_char_code, internal_key_char_code, operation):
        if operation == "encrypt":
            transformed_code = (char_code + key_char_code + internal_key_char_code) % 256
        else:  # decrypt
            transformed_code = (char_code - key_char_code - internal_key_char_code) % 256
        return transformed_code

    def encrypt(self, text):
        encrypted_text = ""
        key_length = len(self.key)
        internal_key_length = len(self.internal_decrypt_key)
        for i, char in enumerate(text):
            key_char_code = ord(self.key[i % key_length])
            internal_key_char_code = ord(self.internal_decrypt_key[i % internal_key_length])
            
            encrypted_char_code = self._transform_char(ord(char), key_char_code, internal_key_char_code, "encrypt")
            encrypted_text += chr(encrypted_char_code)
        return encrypted_text
    
    def decrypt(self, encrypted_text):
        decrypted_text = ""
        key_length = len(self.key)
        internal_key_length = len(self.internal_decrypt_key)
        for i, char in enumerate(encrypted_text):
            key_char_code = ord(self.key[i % key_length])
            internal_key_char_code = ord(self.internal_decrypt_key[i % internal_key_length])
            
            decrypted_char_code = self._transform_char(ord(char), key_char_code, internal_key_char_code, "decrypt")
            decrypted_text += chr(decrypted_char_code)
        return decrypted_text

users_data = {
    "user": "rafas",
    "key": "123456789"
}

users_data_2 = {
    "user": "ksr",
    "key": "123456789"
}

cipher = RafasCrypt(users_data["key"])

encrypted_rafas_user = cipher.encrypt(users_data["user"])
encrypted_rafas_key = cipher.encrypt(users_data["key"])

cipher_2 = RafasCrypt(users_data_2["key"])
encrypted_ksr_user = cipher_2.encrypt(users_data_2["user"])
encrypted_ksr_key = cipher_2.encrypt(users_data_2["key"])

print(f"Encrypted rafas user: {base64.b64encode(encrypted_rafas_user.encode()).decode()}")
print(f"Encrypted rafas key: {base64.b64encode(encrypted_rafas_key.encode()).decode()}")
print(f"Encrypted ksr user: {base64.b64encode(encrypted_ksr_user.encode()).decode()}")
print(f"Encrypted ksr key: {base64.b64encode(encrypted_ksr_key.encode()).decode()}")

decrypted_rafas_user = cipher.decrypt(encrypted_rafas_user)
decrypted_rafas_key = cipher.decrypt(encrypted_rafas_key)
decrypted_ksr_user = cipher_2.decrypt(encrypted_ksr_user)
decrypted_ksr_key = cipher_2.decrypt(encrypted_ksr_key)

print(f"Decrypted rafas user: {decrypted_rafas_user}")
print(f"Decrypted rafas key: {decrypted_rafas_key}")
print(f"Decrypted ksr user: {decrypted_ksr_user}")
print(f"Decrypted ksr key: {decrypted_ksr_key}")


