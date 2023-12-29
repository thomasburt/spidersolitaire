class Column(object):
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
    
    def check_king_to_ace(self):
        pass

    def can_move_stack(self):
        return True

    def can_drop_stack(self):
        return True