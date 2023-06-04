from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from letter import Letter
    from letterbox import LetterBox

from post_office import PostOffice


class Postie:
    def __init__(self) -> None:
        self.letters: list[Letter] = []
        self.route: set[LetterBox] = set()

    def deliver_letters(self) -> None:
        for address in self.route:
            if len(self.letters) == 0:
                break
            for idx, letter in enumerate(self.letters):
                if letter.addressee == address.address:
                    letter_added = address.add_letter(letter)
                    if letter_added:
                        self.letters.pop(idx)

    def collect_postoffice_letters(self, postoffice: PostOffice) -> None:
        for letter in postoffice.stored_letters:
            for serviced_address in postoffice.serviced_addresses:
                if letter.addressee == serviced_address.address:
                    self.route.add(serviced_address)
                    self.letters.append(letter)
