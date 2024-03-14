from models.deck import Deck

class Player:
    """class representing a player object
    instance variables: 
    1) player_name
    2) a reference to the deck they are using
    3) their current hand
    """

    def __init__(self, name, deck: Deck) -> None:
        self.name = name
        self.deck = deck
        self.hand = []

    def draw_cards(self, numCards):
        self.hand = Deck.deal(self.deck,numCards)
    
    def show_hand(self):
        print(self.hand)