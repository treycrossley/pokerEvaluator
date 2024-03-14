from collections import defaultdict

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
    for card_value in range(2,15):
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

def get_high_card(hand):
    max = 2
    for card in hand:
        if (get_value(card) > max):
            max = get_value(card)
    return max



def group_by_rank(players_info):
    grouped = {}
    for player_data in players_info:
        rank= player_data[2]
        value = [player_data[0], player_data[1]]
        if rank in grouped:
            grouped[rank].append(value)
        else:
            grouped[rank] = [value]
    return grouped

def compare_royal_flush(competitors):
    return competitors

def compare_straight_flush(competitors):
    rank = 8
    for competitor in competitors:
        hand = competitor[1]
        frac = get_straight_high_card(hand)/15
        competitor.append(frac+rank)
    return competitors

def compare_4kind(competitors):
    rank = 7
    for competitor in competitors:
        hand = competitor[1]
        frac = get_card_count(hand,4)/15
        competitor.append(frac+rank)
    return competitors

def compare_full_house(competitors):
    rank = 6
    for competitor in competitors:
        hand = competitor[1]
        frac = get_card_count(hand,3)/15
        competitor.append(frac+rank)
    return competitors

def compare_flush(competitors):
    rank = 5
    for competitor in competitors:
        hand = competitor[1]
        frac = get_high_card(hand)/15
        competitor.append(frac+rank)
    return competitors

def compare_straight(competitors):
    rank = 4
    for competitor in competitors:
        hand = competitor[1]
        frac = get_straight_high_card(hand)/15
        competitor.append(frac+rank)
    return competitors

def compare_3kind(competitors):
    rank = 3
    for competitor in competitors:
        hand = competitor[1]
        frac = get_card_count(hand,3)/15
        competitor.append(frac+rank)
    return competitors

def filter_hand(hand, numToRemove):
    return filter(lambda card: get_value(card) != numToRemove, hand)

def compare_2pair(competitors):
    rank = 2
    for competitor in competitors:
        hand = competitor[1]
        pair1 = get_card_count(hand,2)
        frac = pair1/20

        subHand = filter_hand(hand,pair1)
        pair2 = get_card_count(subHand,2)
        frac += pair2/200

        subHand = filter_hand(subHand, pair2)
        kicker = get_high_card(subHand)
        frac += kicker/2000
        
        competitor.append(frac+rank)
    return[]


def compare_pair(competitors):
    rank = 1
    for competitor in competitors:
        hand = competitor[1]
        pairNum = get_card_count(hand,2)
        frac = pairNum/20

        subHand = filter_hand(hand,pairNum)
        kicker = get_high_card(subHand)
        frac += kicker/200

        subHand = filter_hand(subHand, kicker)
        kicker = get_high_card(subHand)
        frac += kicker/2000

        subHand = filter_hand(subHand, kicker)
        kicker = get_high_card(subHand)
        frac += kicker/20000

        competitor.append(frac+rank)
    return competitors

def compare_high_card(competitors):
    rank = 0
    for competitor in competitors:
        hand = competitor[1]
        frac = get_high_card(hand)/15
        competitor.append(frac+rank)
    return competitors


def eval_tie(rank, competitors):
    if(rank == 9):
        return compare_royal_flush(competitors)
    if(rank == 8):
        return compare_straight_flush(competitors)
    if(rank == 7):
        return compare_4kind(competitors)
    if(rank == 6):
        return compare_full_house(competitors)
    if(rank == 5):
        return compare_flush(competitors)
    if(rank == 4):
        return compare_straight(competitors)
    if(rank == 3):
        return compare_3kind(competitors)
    if(rank == 2):
        return compare_2pair(competitors)
    if(rank == 1):
        return compare_pair(competitors)   
    return compare_high_card(competitors)

def eval_tiebreakers(players_info):
    result = []
    # separate tuples by rank groups
    grouped = group_by_rank(players_info)
    # evaluate tie breakers for each individual rank
    for rank, competitors in grouped.items():
        if len(competitors) == 1:
            player = [competitors[0][0], competitors[0][1], rank]
            result.append(player)
            continue
        else:
            result.extend(eval_tie(rank, competitors))
    return result


def determine_player_rankings(player_hands):
    players_info = []
    for player,hand in player_hands.items():
        rank = rank_hand(hand)
        player_data = [player, hand, rank]
        players_info.append(player_data)
    players_info = eval_tiebreakers(players_info)
    return players_info

def determine_winner(player_hands):
    results = determine_player_rankings(player_hands)
    max = 0
    for res in results:
        rank = res[2]
        if max < rank:
            max = rank
    winner = ""
    for res in results:
        rank = res[2]
        if rank == max:
            name = res[0]
            winner += name + ","
    winner = winner[:-1]
    return winner

    
    
