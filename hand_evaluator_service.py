
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

def get_card_frequency(hand):
    freq = {card:0 for card in range(1,15)} #initialize card dict with zero occurences
    for card in hand:
        val = get_value(card)
        freq[val] += 1
    freq[1] = freq[14] #Ace high/low case
    return freq
    

def get_straight_high_card(hand):
    freq = get_card_frequency(hand)
    for val in range(1,11):
        if all([freq[val + i] == 1 for i in range(0,5)]):
            return val + 4
    return None

def get_card_count(hand, num_occurences, ignore_card=None):
    freq = get_card_frequency(hand)
    for card_value in range(1,14):
        if(card_value != ignore_card and freq[card_value] == num_occurences):
            return card_value
    return None    
    
