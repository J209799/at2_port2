from typing import NamedTuple


class _letter_return(NamedTuple):
    is_read: bool
    letter_content: str

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class Letter:
    """Represents a letter."""

    def __init__(self, content: str, addressee: str, key: str) -> None:
        self._isread = False
        self.content: str = Letter._encrypt(content, key)
        self.addressee = addressee

    def read_letter(self, key: str) -> tuple[bool, str]:
        if self._isread is True:
            return _letter_return(True, Letter._decrypt(self.content, key))
        self._isread = True
        return _letter_return(False, Letter._decrypt(self.content, key))

    @staticmethod
    def _encrypt(content: str, key: str) -> str:
        ciphertext = ""
        key_index = 0

        for char in content:
            if char.upper() in alphabet:
                shift = alphabet.index(key[key_index].upper())
                encrypted_char = alphabet[(alphabet.index(char.upper()) + shift) % 26]
                ciphertext += encrypted_char if char.isupper() else encrypted_char.lower()
                key_index = (key_index + 1) % len(key)
            else:
                ciphertext += char
        return ciphertext

    @staticmethod
    def _decrypt(content: str, key: str) -> str:
        # just do the opposite of the encrypt method
        plaintext = ""
        key_index = 0

        for char in content:
            if char.upper() in alphabet:
                shift = alphabet.index(key[key_index].upper())
                decrypted_char = alphabet[(alphabet.index(char.upper()) - shift) % 26]
                plaintext += decrypted_char if char.isupper() else decrypted_char.lower()
                key_index = (key_index + 1) % len(key)
            else:
                plaintext += char
        return plaintext
