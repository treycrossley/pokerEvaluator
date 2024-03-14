class Card:

    def __init__(self, suit, val):
        self.suit = suit
        self.val = val

    @staticmethod
    def decode_suit_from_string(card_string):
        str_length = len(card_string)
        return card_string[str_length-1:].lower()
    
    @staticmethod
    def decode_val_from_string(card_string):
        str_length = len(card_string)
        return card_string[:str_length - 1]


    def get_suit(self):
        return self.suit
    
    def get_rank(self):
        return self.val
    
    def show(self):
        print("Suit: {}, Rank: {}".format(self.suit, self.val))
