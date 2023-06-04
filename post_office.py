from letter import Letter
from letterbox import LetterBox


class PostOffice:

    def __init__(self, serviced_addresses: set[LetterBox]) -> None:
        self.serviced_addresses: set[LetterBox] = serviced_addresses
        self.stored_letters: list[Letter] = []

    def add_address(self, address: LetterBox) -> bool:
        if address in self.serviced_addresses:
            return False
        else:
            self.serviced_addresses.add(address)
            return True

    def add_letter(self, letter: Letter) -> None:
        self.stored_letters.append(letter)

