class VigenereCipher:

    def __init__(self):
        pass

    def validate_key(self, key):
        if not key:
            raise ValueError("Key cannot be empty")

        if not key.isalpha():
            raise ValueError("Key must contain only letters")

    def encrypt_text(self, plain_text, key):

        self.validate_key(key)

        encrypted_text = ""
        key_index = 0

        for char in plain_text:

            if char.isalpha():

                key_shift = ord(
                    key[key_index % len(key)].upper()
                ) - ord('A')

                base = ord('A') if char.isupper() else ord('a')

                encrypted_text += chr(
                    (ord(char) - base + key_shift) % 26 + base
                )

                key_index += 1

            else:
                encrypted_text += char

        return encrypted_text

    def decrypt_text(self, encrypted_text, key):

        self.validate_key(key)

        decrypted_text = ""
        key_index = 0

        for char in encrypted_text:

            if char.isalpha():

                key_shift = ord(
                    key[key_index % len(key)].upper()
                ) - ord('A')

                base = ord('A') if char.isupper() else ord('a')

                decrypted_text += chr(
                    (ord(char) - base - key_shift) % 26 + base
                )

                key_index += 1

            else:
                decrypted_text += char

        return decrypted_text