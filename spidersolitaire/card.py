class Card:
    def __init__(self, value, suit) -> None:
        self.value = value
        self.suit = suit
        self.image = self.get_image()

    def get_image(self):
        pass

    