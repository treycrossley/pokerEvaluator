

suitMap = {
    "h": "hearts",
    "d": "diamonds",
    "c": "clubs",
    "s": "spades"
}

rankMap = {
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
    "J": "Jack",
    "Q": "Queen",
    "K": "King",
    "A": "Ace"

}

class Card:
    """class representing a Card object
    instance variables: 
    1) card suit
    2) card value
    """
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val

    def get_suit(self):
        return self.suit
    
    def get_rank(self):
        return self.val
    
    def show(self):
        print("{} of {}".format(rankMap(self.val), suitMap(self.suit)))
