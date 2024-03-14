
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

def rank_hand(hand):
    if get_straight_high_card(hand) == 14 and is_flush(hand):
        return 9 #Royal Flush
    if get_straight_high_card(hand) is not None and is_flush(hand):
        return 8 #Straight Flush
    if get_card_count(hand,4) is not None:
        return 7 #4 of a Kind
    if get_card_count(hand, 3) is not None and get_card_count(hand, 2) is not None:
        return 6 #Full House
    if is_flush(hand):
        return 5 #Flush
    if get_straight_high_card(hand) is not None:
        return 4 #Straight
    if get_card_count(hand,3) is not None:
        return 3 #3 of a kind
    pair1 = get_card_count(hand, 2)
    if pair1 is not None:
        if get_card_count(hand, 2, pair1) is not None:
            return 2 #two pair
        return 1 # pair
    return 0 #High Card

def display_rank(rank):
    rank_map = {
        9: "Royal Flush",
        8: "Straight Flush",
        7: "Four of a Kind",
        6: "Full House",
        5: "Flush",
        4: "Straight",
        3: "Three of a Kind",
        2: "Two Pair",
        1: "Pair",
        0: "High Card"
    }

    return rank_map[rank]


    
    
