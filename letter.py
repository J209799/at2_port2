from typing import NamedTuple


class _letter_return(NamedTuple):
    is_read: bool
    letter_content: str


class Letter:
    """Represents a letter."""

    def __init__(self, content: str, key: int) -> None:
        self._isread = False
        self.content: str = Letter._encrypt(content, key)

    def read_letter(self, key: int) -> tuple[bool, str]:
        if self._isread is True:
            return _letter_return(True, Letter._decrypt(self.content, key))
        self._isread = True
        return _letter_return(False, Letter._decrypt(self.content, key))

    @staticmethod
    def _encrypt(content: str, key: int) -> str:
        encrypted_array: list[str] = []
        offset = 1
        for word in content.split():
            encrypted_word = ""
            for letter in word:
                # Get the Unicode code with ord, then offset with the offset and key.
                # then conver that unicode code back into a unicode character
                encrypted_word += chr((ord(letter) + offset) + key)
            encrypted_array.append(encrypted_word)
            # increase the offset for each word
            offset += 1
        return " ".join(encrypted_array)

    @staticmethod
    def _decrypt(content: str, key: int):
        # just do the opposite of the encrypt method
        decrypted_array: list[str] = []
        offset = 1
        for word in content.split():
            decrypted_word = ""
            for letter in word:
                decrypted_word += chr((ord(letter) - offset) - key)
            decrypted_array.append(decrypted_word)
            offset += 1
        return " ".join(decrypted_array)
