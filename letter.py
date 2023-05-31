from typing import NamedTuple


class _letter_return(NamedTuple):
    is_read: bool
    letter_content: str


class Letter:
    """Represents a letter."""

    def __init__(self, content: str) -> None:
        self._isread = False
        self.content = content

    def read_letter(self) -> tuple[bool, str]:
        if self._isread is True:
            return _letter_return(True, self.content)
        self._isread = True
        return _letter_return(False, self.content)
