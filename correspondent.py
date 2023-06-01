from typing import Self

from letter import Letter
from letterbox import LetterBox


class Correspondent:
    def __init__(self, name: str, recipient_address: str, address: str) -> None:
        self.name = name
        self.letterbox = LetterBox(self)
        self.recipient_address = recipient_address

    def read_letterbox_letter(self) -> str | None:
        letter = self.letterbox.get_letter()
        if letter is None:
            return None
        letter = letter.read_letter()
        return f"Already read?: {letter.is_read}\n{letter.letter_content}"

    def send_letter(self, recipient: Self, letter: Letter) -> bool:
        send_result = recipient.letterbox.add_letter(letter)
        return send_result
