from correspondent import Correspondent
from letter import Letter

if __name__ == "__main__":
    alice = Correspondent("Alice")
    bob = Correspondent("Bob")
    bobs_letter = Letter("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
    bob.send_letter(alice, bobs_letter)
    if alice.letterbox.has_letter:
        print(alice.read_letterbox_letter())
