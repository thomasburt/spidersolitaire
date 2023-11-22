import card
import deck
import column
import stack
import pygame
import pygame_menu

class SpiderSolitaire:
    SPADES = card.Card.SPADES
    HEARTS = card.Card.HEARTS
    DIAMONDS = card.Card.DIAMONDS
    CLUBS = card.Card.CLUBS

    EASY_DIFFICULTY = { 8: SPADES }
    MEDIUM_DIFFICULTY = { 4: SPADES, 4: HEARTS }
    HARD_DIFFICULTY = { 2: SPADES, 2: HEARTS, 2: CLUBS, 2: DIAMONDS }
    
    def __init__(self) -> None:
        self.deck = None
        self.playarea = [ column.Column() for x in range(10) ]
        self.stack = None
        self.menu = None
        self.difficulty = None

        pygame.init()
        self.surface = pygame.display.set_mode((800, 600))

    def is_valid_move(self, source_col, dest_col):
        pass

    def move(self, source_col, dest_col):
        pass

    def check_win_condition(self):
        pass
    
    def display(self):
        pass

    def set_difficulty(self, value, difficulty):
        if difficulty == 1:
            self.difficulty = SpiderSolitaire.EASY_DIFFICULTY
        elif difficulty == 2:
            self.difficulty = SpiderSolitaire.MEDIUM_DIFFICULTY
        elif difficulty == 3:
            self.difficulty = SpiderSolitaire.HARD_DIFFICULTY

    def game(self):
        self.deck = deck.Deck(self.difficulty)

        for i in range(54):
            self.playarea[i % 10].add_card(self.deck.draw())

        for column in self.playarea:
            column.get_top_card().flip()

    def boot(self):
        self.menu = pygame_menu.Menu('Welcome to Spider Solitaire', 400, 300, theme=pygame_menu.themes.THEME_BLUE)
        self.menu.add.selector('Difficulty: ', [('Easy', 1), ('Medium', 2), ('Hard', 3)], onchange=self.set_difficulty)
        self.menu.add.button('Play', self.game)
        self.menu.add.button('Quit', pygame_menu.events.EXIT)

        self.menu.mainloop(self.surface)

if __name__ == '__main__':
    game = SpiderSolitaire()
    game.boot()