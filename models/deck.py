import random 

class Deck:
    """class representing a deck object
    instance variables: 
    1) the deck of 52 cards. This deck can be shuffled and cards can be removed as they are dealt to other players
    """

    def __init__(self) -> None:
        self.deck = self.create_shuffled_deck()

    def get_deck(self):
        return self.deck

    def create_deck(self):
        #initializes a deck with all 52 cards
        deck = []
        for suit in ("c", "d", "h", "s"):
            for card in range(2,15):
                if card < 11:
                    val_string = str(card)
                else:
                    val_string = ("J", "Q", "K", "A")[card - 11]
                deck.append(val_string + suit)
        return deck
    
    def shuffle_deck(self, deck):
        random.shuffle(deck)
        return deck
    
    def create_shuffled_deck(self):
        deck = self.create_deck()
        return self.shuffle_deck(deck)
    
    def deal(self, numCards=5):
        if(self.num_cards_left() < numCards): return False

        hand = self.deck[:numCards]
        del self.deck[:numCards]
        return hand
    
    def num_cards_left(self):
        return len(self.deck)
    


