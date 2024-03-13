class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank  

    def __init__(self, card_string):
        self.suit = self.decode_suit_from_string(card_string)
        self.rank = self.decode_rank_from_string(card_string)

    def decode_suit_from_string(card_string):
        str_length = len(card_string)
        return card_string[str_length-1:].lower()
    
    def decode_rank_from_string(card_string):
        str_length = len(card_string)
        return card_string[:str_length - 1]


    def get_suit(self):
        return self.suit
    
    def get_rank(self):
        return self.rank
    
    def print_card(self):
        print("Suit: {}, Rank: {}".format(self.suit, self.rank))
