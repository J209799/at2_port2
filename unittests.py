import unittest

from correspondent import Correspondent
from letter import Letter, _letter_return
from letterbox import LetterBox
from post_office import PostOffice
from postie import Postie


class LetterTest(unittest.TestCase):
    def test_read_letter(self):
        letter = Letter("Hello, World!", "ABC", "YOLO")
        self.assertEqual(letter.read_letter("YOLO"), _letter_return(False, "Hello, World!"))
        self.assertEqual(letter.read_letter("YOLO"), _letter_return(True, "Hello, World!"))

    def test_encryption(self):
        letter = Letter("Hello, World!", "ABC", "YOLO")
        self.assertEqual("Fswzm, Kzfjr!", letter.content) # from vigenere-cipher

    def test_decryption(self):
        letter = Letter("Hello, World!", "ABC", "YOLO")
        decrypted_content = letter.read_letter("YOLO")
        self.assertEqual("Hello, World!", decrypted_content.letter_content)



class CorrespondentTest(unittest.TestCase):
    def test_read_letterbox_letter(self):
        letter = Letter("Hello, world!", "Alice", "key")
        correspondent = Correspondent("Bob", "123 Street", "key")
        correspondent.letterbox.add_letter(letter)
        expected_output = "Already read?: False\nHello, world!"
        self.assertEqual(correspondent.read_letterbox_letter(), expected_output)

    def test_send_letter(self):
        correspondent = Correspondent("Alice", "456 Street", "key")
        postoffice = PostOffice({correspondent.letterbox})
        correspondent.send_letter("Hello, world!", "Bob", "key", postoffice)
        self.assertEqual(postoffice.stored_letters[0].addressee, "Bob")
        self.assertEqual(postoffice.stored_letters[0]._encrypt("Hello, world!", "key"), postoffice.stored_letters[0].content)

    def test_read_letterbox_letter_when_no_letter(self):
        correspondent = Correspondent("Bob", "123 Street", "key")
        self.assertIsNone(correspondent.read_letterbox_letter())


class LetterBoxTest(unittest.TestCase):
    def test_add_letter(self):
        letter = Letter("Hello, world!", "Alice", "key")
        letter_box = LetterBox("Bob", "123 Street")
        self.assertTrue(letter_box.add_letter(letter))
        self.assertTrue(letter_box.has_letter)
        self.assertEqual(letter_box.get_letter(), letter)

    def test_add_letter_in_full_letterbox(self):
        letter1 = Letter("AAAA", "Alice", "key")
        letter2 = Letter("BBBB", "Alice", "key")
        letter_box = LetterBox("Bob", "123 Street")

        self.assertTrue(letter_box.add_letter(letter1))
        self.assertFalse(letter_box.add_letter(letter2))
        self.assertTrue(letter_box.has_letter)
        self.assertEqual(letter_box.get_letter(), letter1)

    def test_get_letter_from_empty_letterbox(self):
        letter_box = LetterBox("X", "A")
        self.assertIsNone(letter_box.get_letter())


class PostOfficeTest(unittest.TestCase):
    def test_add_address(self):
        letter_box = LetterBox("Bob", "123 Street")
        post_office = PostOffice(set())
        self.assertTrue(post_office.add_address(letter_box))
        self.assertIn(letter_box, post_office.serviced_addresses)

    def test_add_existing_address(self):
        letter_box = LetterBox("Bob", "123 Street")
        post_office = PostOffice({letter_box})
        self.assertFalse(post_office.add_address(letter_box))

    def test_add_letter(self):
        letter = Letter("Hello, world!", "Alice", "key")
        post_office = PostOffice(set())
        post_office.add_letter(letter)
        self.assertEqual(post_office.stored_letters, [letter])


class PostieTest(unittest.TestCase):
    def test_deliver_letters(self):
        letter1 = Letter("X", "ADDRESS_1", "key")
        letter2 = Letter("Y", "ADDRESS_2", "key")
        postie = Postie()
        postie.letters = [letter1, letter2]
        address1 = LetterBox("Alice", "ADDRESS_1")
        address2 = LetterBox("Bob", "ADDRESS_2")
        postie.route = {address1, address2}
        postie.deliver_letters()
        self.assertTrue(address1.has_letter)
        self.assertEqual(address1.get_letter(), letter1)

        self.assertTrue(address2.has_letter)
        self.assertEqual(address2.get_letter(), letter2)


    def test_collect_postoffice_letters(self):
        letter1 = Letter("X", "ADDRESS_1", "key")
        letter2 = Letter("Y", "ADDRESS_2", "key")
        address1 = LetterBox("Alice", "ADDRESS_1")
        address2 = LetterBox("Bob", "ADDRESS_2")
        postoffice = PostOffice({address1, address2})
        postoffice.add_letter(letter1)
        postoffice.add_letter(letter2)
        postie = Postie()
        postie.collect_postoffice_letters(postoffice)
        self.assertEqual(postie.letters, [letter1, letter2])
        self.assertEqual(postie.route, {address1, address2})


if __name__ == "__main__":
    unittest.main()
