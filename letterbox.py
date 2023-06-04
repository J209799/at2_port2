from typing import Any

from letter import Letter


class LetterBox:
    def __init__(self, owner: Any, address: str) -> None:
        self._owner = owner
        self.has_letter: bool = False
        self.letter: Letter | None = None
        self.address: str = address

    def add_letter(self, new_letter: Letter) -> bool:
        if self.has_letter:
            return False
        self.letter = new_letter
        self.has_letter = True
        return True

    def get_letter(self) -> Letter | None:
        if not self.has_letter:
            return None
        self.has_letter = False
        _tmp_letter = self.letter
        self.letter = None
        return _tmp_letter
