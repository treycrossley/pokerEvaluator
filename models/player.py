from models.deck import Deck

class Player:

    def __init__(self, name, deck: Deck) -> None:
        self.name = name
        self.deck = deck
        self.hand = []

    def draw_cards(self, numCards):
        self.hand = Deck.deal(self.deck,numCards)
    
    def show_hand(self):
        print(self.hand)