from collections import defaultdict

def get_suit(card_string):
    """Takes in card string and returns the character representing the card suit

    Parameter:
    card_string (string): a string in the format of "VALUEsuit"
    examples include "10c", "Jd", "Qh"

    Returns:
    returns the char representing the first letter of the suit (ie. h = heart, c = club)  
    """
    return card_string[-1]

def get_value(card_string):
    """Takes in card string and returns the numerical value of the card

    Parameter:
    card_string (string): a string in the format of "VALUEsuit"
    examples include "10c", "Jd", "Qh"

    Returns:
    returns an int in the numerical value of the card
    """
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
    """Tests if a given hand is a flush

    Parameter:
    hand (list<card_string>) a list of strings where each string represents a card

    Returns:
    a boolean that determines if the hand is a flush
    """
    card_suits = set(map(get_suit,hand))
    return len(card_suits) == 1

def get_card_frequency(hand):
    """Takes hand and returns a dictionary describing the frequency of each card occuring in the hand

    Parameter:
    hand (list<card_string>) a list of strings where each string represents a card

    Returns:
    a dictionary in the form of { cardVal: numOfOccurences }.
    """
    freq = {card:0 for card in range(1,15)} #initialize card dict with zero occurences
    for card in hand:
        val = get_value(card)
        freq[val] += 1
    freq[1] = freq[14] #Ace high/low case
    return freq
    

def get_straight_high_card(hand):
    """Tests if given hand is a straight. If so returns the highest card in the straight. otherwise returns none

    Parameter:
    hand (list<card_string>) a list of strings where each string represents a card

    Returns:
    The highest card in any detected straight. if no straight detected, returns None
    """
    freq = get_card_frequency(hand)
    for val in range(1,11):
        if all([freq[val + i] == 1 for i in range(0,5)]):
            return val + 4
    return None

def get_card_count(hand, num_occurences, ignore_card=None):
    """returns the card value that occurs the specified number of times

    Parameter:
    hand: (list<card_string>) a list of strings where each string represents a card
    num_occurences: the number of times we want the card to repeat (if we're looking for 4-of-a-kind, this number would be 4)
    ignore_card: ignores this specific number during search. Mostly used during the two-pair check

    Returns:
    returns the card value in int form with the specified count
    """
    freq = get_card_frequency(hand)
    for card_value in range(2,15):
        if(card_value != ignore_card and freq[card_value] == num_occurences):
            return card_value
    return None    

def rank_hand(hand):
    """Given a hand, determines which hand it is

    Parameter:
    hand: (list<card_string>) a list of strings where each string represents a card

    Returns:
    returns an int that represents the rank of the hand
    """
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
    """Given a numerical rank, converts the number to a string for easy reading

    Parameter:
    rank: numeric value representing the card combination in a hand

    Returns:
    returns a string representing the display value for that rank number
    """
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
    """Given a hand, returns the highest cardVal found

    Parameter:
    hand: (list<card_string>) a list of strings where each string represents a card

    Returns:
    returns an int representing the highest card value found
    """
    max = 2
    for card in hand:
        if (get_value(card) > max):
            max = get_value(card)
    return max



def group_by_rank(players_info):
    """Given all the player's info, groups players into a dictionary by their hand rank (1 for pair, 2 for two pair, etc)

    Parameter:
    players_info: a 2D list: Each row contains the follwing columns, player_name, player_hand, hand_rank

    Returns:
    returns a dictionary where the hand_rank is the key and the value is a list of players and their hands that have that rank
    """
    grouped = {}
    print("PLAYER INFO: " +str(players_info))
    for player_data in players_info:
        rank= player_data[2]
        value = [player_data[0], player_data[1]]
        if rank in grouped:
            grouped[rank].append(value)
        else:
            grouped[rank] = [value]
    return grouped


def compare_straight_flush(competitors):
    """Determines who wins the tie breaker between straight flushes

    Parameter:
    competitors: a list of of player info (player_name, hand, rank)

    Returns:
    returns a list of competitors with updated rank to differentiate between which straight-flush wins the tiebreaker
    """
    rank = 8
    for competitor in competitors:
        hand = competitor[1]
        frac = get_straight_high_card(hand)/15 #arbitrary number to add additional precision to competition within rank
        competitor.append(frac+rank)
    return competitors

def compare_4kind(competitors):
    """Determines who wins the tie breaker between 4 of a kind hands

    Parameter:
    competitors: a list of of player info (player_name, hand, rank)

    Returns:
    returns a list of competitors with updated rank to differentiate between which straight-flush wins the tiebreaker
    """
    rank = 7
    for competitor in competitors:
        hand = competitor[1]
        frac = get_card_count(hand,4)/15 #arbitrary number to add additional precision to competition within rank
        competitor.append(frac+rank)
    return competitors

def compare_full_house(competitors):
    """Determines who wins the tie breaker between full house hands

    Parameter:
    competitors: a list of of player info (player_name, hand, rank)

    Returns:
    returns a list of competitors with updated rank to differentiate between which wins the tiebreaker
    """
    rank = 6
    for competitor in competitors:
        hand = competitor[1]
        frac = get_card_count(hand,3)/15 #arbitrary number to add additional precision to competition within rank
        competitor.append(frac+rank)
    return competitors

def compare_flush(competitors):
    """Determines who wins the tie breaker between flush hands

    Parameter:
    competitors: a list of of player info (player_name, hand, rank)

    Returns:
    returns a list of competitors with updated rank to differentiate between which wins the tiebreaker
    """
    rank = 5
    for competitor in competitors:
        hand = competitor[1]
        frac = get_high_card(hand)/15 #arbitrary number to add additional precision to competition within rank
        competitor.append(frac+rank)
    return competitors

def compare_straight(competitors):
    """Determines who wins the tie breaker between straight hands

    Parameter:
    competitors: a list of of player info (player_name, hand, rank)

    Returns:
    returns a list of competitors with updated rank to differentiate between which wins the tiebreaker
    """
    rank = 4
    for competitor in competitors:
        hand = competitor[1]
        frac = get_straight_high_card(hand)/15 #arbitrary number to add additional precision to competition within rank
        competitor.append(frac+rank)
    return competitors

def compare_3kind(competitors):
    """Determines who wins the tie breaker between 3 of a kind hands

    Parameter:
    competitors: a list of of player info (player_name, hand, rank)

    Returns:
    returns a list of competitors with updated rank to differentiate between which  wins the tiebreaker
    """
    rank = 3
    for competitor in competitors:
        hand = competitor[1]
        frac = get_card_count(hand,3)/15 #arbitrary number to add additional precision to competition within rank
        competitor.append(frac+rank)
    return competitors

def filter_hand(hand, numToRemove):
    """Filters hand based on a number to remove

    Parameter:
    hand: a list of strings representing cards. 
    numToRemove: the cardVal we want removed from the hand

    Returns:
    a new hand without the filtered cards
    """
    return filter(lambda card: get_value(card) != numToRemove, hand)

def compare_2pair(competitors):
    """Determines who wins the tie breaker between two-pair hands

    Parameter:
    competitors: a list of of player info (player_name, hand, rank)

    Returns:
    returns a list of competitors with updated rank to differentiate between which wins the tiebreaker
    """
    rank = 2
    for competitor in competitors:
        hand = competitor[1]
        pair1 = get_card_count(hand,2)
        frac = pair1/20 #arbitrary number to add additional precision to competition within rank

        subHand = filter_hand(hand,pair1)
        pair2 = get_card_count(subHand,2)
        frac += pair2/200 #smaller frac to differentiate between tie breaker cases and should not overflow the previous frac

        subHand = filter_hand(subHand, pair2)
        kicker = get_high_card(subHand)
        frac += kicker/2000 #smaller frac to differentiate between tie breaker cases and should not overflow the previous frac
        
        competitor.append(frac+rank)
    return[]


def compare_pair(competitors):
    """Determines who wins the tie breaker between 1pair hands

    Parameter:
    competitors: a list of of player info (player_name, hand, rank)

    Returns:
    returns a list of competitors with updated rank to differentiate between which wins the tiebreaker
    """
    rank = 1
    for competitor in competitors:
        hand = competitor[1]
        pairNum = get_card_count(hand,2)
        frac = pairNum/20 #arbitrary number to add additional precision to competition within rank

        subHand = filter_hand(hand,pairNum)
        kicker = get_high_card(subHand)
        frac += kicker/200 #smaller frac to differentiate between tie breaker cases and should not overflow the previous frac

        subHand = filter_hand(subHand, kicker)
        kicker = get_high_card(subHand)
        frac += kicker/2000 #smaller frac to differentiate between tie breaker cases and should not overflow the previous frac

        subHand = filter_hand(subHand, kicker)
        kicker = get_high_card(subHand)
        frac += kicker/20000 #smaller frac to differentiate between tie breaker cases and should not overflow the previous frac

        competitor.append(frac+rank)
    return competitors

def compare_high_card(competitors):
    """Determines who wins the tie breaker between high cards

    Parameter:
    competitors: a list of of player info (player_name, hand, rank)

    Returns:
    returns a list of competitors with updated rank to differentiate between which wins the tiebreaker
    """
    rank = 0
    for competitor in competitors:
        hand = competitor[1]
        frac = get_high_card(hand)/15 #arbitrary number to add additional precision to competition within rank
        competitor.append(frac+rank)
    return competitors


def eval_tie(rank, competitors):
    """Determines who wins the tie breaker between hands

    Parameter:
    rank: number to determine which tiebreaker function should be used
    competitors: a list of of player info (player_name, hand, rank)

    Returns:
    returns a list of competitors with updated rank to differentiate between which wins the tiebreaker
    """
    if(rank == 9):
        return competitors
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
    """Separates hands into rank groups and evaluates each tiebreaker reference individually

    Parameter:
    players_info: a list of of player info (player_name, hand, rank)

    Returns:
    returns an updated list of competitors with all possible tie-breakers evaluated for
    """
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
    """Calculates the rankings of players based on the cards in their hand

    Parameter:
    player_hands: a 2d list, where each row contains a list of player_names and their hands

    Returns:
    returns a list of competitors with their rankings in the round
    """
    players_info = []
    for player,hand in player_hands.items():
        rank = rank_hand(hand)
        player_data = [player, hand, rank]
        players_info.append(player_data)
    return eval_tiebreakers(players_info)
    

def determine_winner(player_hands):
    """Determines the overall winner of the round

    Parameter:
    player_hands: a 2d list, where each row contains a list of player_names and their hands

    Returns:
    returns a string of all the players who had the maximum found hand Value this round
    """
    results = determine_player_rankings(player_hands)
    max = 0
    #Find max rank
    for res in results:
        rank = res[2]
        if max < rank:
            max = rank
    winner = ""
    #For all players whose hand represents the max rank, add them to the winner list
    for res in results:
        rank = res[2]
        if rank == max:
            name = res[0]
            winner += name + ","
    winner = winner[:-1]
    return winner

    
    
