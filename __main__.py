from correspondent import Correspondent
from post_office import PostOffice
from postie import Postie

if __name__ == "__main__":
    alice = Correspondent("Alice", "ABC43", "AlicesKey")
    bob = Correspondent("Bob", "ATT3", "BobsKey")
    charlie_postie = Postie()
    perth_post_office = PostOffice({bob.letterbox, alice.letterbox})
    bob_letter_content = "Lorem ipsum dolor sit amet, abcdefghi"
    print(bob_letter_content)
    bob.send_letter(
        bob_letter_content,
        "ABC43",
        "AlicesKey",
        perth_post_office,
    )
    charlie_postie.collect_postoffice_letters(perth_post_office)
    charlie_postie.deliver_letters()
    if alice.letterbox.has_letter:
        print(alice.read_letterbox_letter())

