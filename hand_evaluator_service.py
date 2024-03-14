
def get_suit(card_string):
    return card_string[-1]

def get_value(card_string):
    if card_string[0] == "J":
        return 11
    if card_string[0] == "Q":
        return 12
    if card_string[0] == "K":
        return 13
    if card_string[0] == "A":
        return 14
    return int(card_string[0:-1])

def is_flush(hand):
    card_suits = set(map(get_suit,hand))
    return len(card_suits) == 1
    