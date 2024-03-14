

class Card:
    """class representing a Card object
    instance variables: 
    1) card suit
    2) card value
    """

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
        11: "Jack",
        12: "Queen",
        13: "King",
        14: "Ace"
    }


    def __init__(self, suit, val):
        self.suit = suit
        self.val = val

        
    def get_suit(self):
        return self.suit
    
    def get_value(self):
        return self.val
    
    def show(self):
        return ("{} of {}".format(self.rankMap[self.val], self.suitMap[self.suit]))
