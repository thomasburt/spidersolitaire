
class Stack(object):
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop()

    def get_top_card(self):
        if len(self.cards) == 0:
            return None
        return self.cards[-1]

    def get_cards(self):
        return self.cards
    
    def pickup_cards(self):
        self.cards = []
        return 
    
    def validate_dropped_cards(self):
        pass

    def validate_picked_up_cards(self):
        pass