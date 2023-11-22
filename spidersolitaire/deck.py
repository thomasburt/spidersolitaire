
import random
import card

class Deck:
    def __init__(self, difficulty):
        self.cards = []

        for count, suit in difficulty.items():
            for i in range(count):
                for j in range(1,13):
                    self.cards.append(card.Card(j+1, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop()
