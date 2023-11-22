import pathlib
class Card:
    suits = enumerate(["SPADES", "HEARTS", "DIAMONDS", "CLUBS"])
    values = enumerate(["ACE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN",
                        "EIGHT", "NINE", "TEN", "JACK", "QUEEN", "KING"])

    def __init__(self, value, suit):
        self.value = Card.values[value]
        self.suit = Card.suits[suit]
        self.face_up = False
        self.image = pathlib.Path("../images/{}-{}.svg").format(self.value, self.suit)
        self.back_image = pathlib.Path("../images/back-blue.svg")

    def __str__(self):
        return f"{Card.values[self.value]} of {Card.suits[self.suit]}"

    def flip(self):
        if self.face_up:
            self.face_up = False
        else:
            self.face_up = True