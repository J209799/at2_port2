from letter import Letter
from letterbox import LetterBox
from post_office import PostOffice


class Correspondent:
    def __init__(self, name: str, address: str, key: str) -> None:
        self.name = name
        self.letterbox = LetterBox(self, address)
        self._key = key

    def read_letterbox_letter(self) -> str | None:
        letter = self.letterbox.get_letter()
        if letter is None:
            return None
        letter_content = letter.read_letter(self._key)
        return f"Already read?: {letter_content.is_read}\n{letter_content.letter_content}"

    def send_letter(self, content: str, addressee: str, encryption_key: str, post_office: PostOffice) -> None:
        new_letter = Letter(content, addressee, encryption_key)
        post_office.add_letter(new_letter)
