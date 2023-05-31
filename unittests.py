import unittest

from correspondent import Correspondent
from letter import Letter, _letter_return


class LetterTest(unittest.TestCase):
    def test_read_letter(self):
        letter = Letter("Hello, World!")
        self.assertEqual(letter.read_letter(), _letter_return(False, "Hello, World!"))
        self.assertEqual(letter.read_letter(), _letter_return(True, "Hello, World!"))


class CorrespondentTest(unittest.TestCase):
    def test_read_letterbox_letter(self):
        alice = Correspondent("Alice")
        letter_box = alice.letterbox
        letter = Letter("Hello")
        self.assertIsNone(alice.read_letterbox_letter())
        letter_box.add_letter(letter)
        self.assertEqual(alice.read_letterbox_letter(), "Already read?: False\nHello")
        self.assertIsNone(alice.read_letterbox_letter())

    def test_send_letter(self):
        alice = Correspondent("Alice")
        bob = Correspondent("Bob")
        letter = Letter("Hello")
        self.assertTrue(bob.send_letter(alice, letter))  # noqa: PT009
        self.assertFalse(bob.send_letter(alice, letter))  # noqa: PT009


class LetterBoxTest(unittest.TestCase):
    def test_add_letter(self):
        correspondent = Correspondent("Alice")
        letter_box = correspondent.letterbox
        letter = Letter("Hello, World!")
        self.assertTrue(letter_box.add_letter(letter))
        self.assertFalse(letter_box.add_letter(letter))

    def test_get_letter(self):
        correspondent = Correspondent("Alice")
        letter_box = correspondent.letterbox
        letter = Letter("Hello")
        self.assertIsNone(letter_box.get_letter())
        letter_box.add_letter(letter)
        self.assertEqual(letter_box.get_letter(), letter)
        self.assertIsNone(letter_box.get_letter())


if __name__ == "__main__":
    unittest.main()
