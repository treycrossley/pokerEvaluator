from models.deck import Deck
import services.hand_evaluator_service as hand_evaluator_service

# Part 1
def hand_ranking(hand): 
    """Given a list of cards, determine what ranking it has

    Parameter:
    hand: a list of card_strings

    Returns:
    returns a string that identifies the poker hand
    """
    hand_rank = hand_evaluator_service.rank_hand(hand)   
    return hand_evaluator_service.display_rank(hand_rank)

# Part 2
def deal_cards(player_list):
    """Given a list of players, deal each of them 5 cards from the deck

    Parameter:
    hand: a list of players

    Returns:
    returns a dictionary of each player and their hands
    """
    deck = Deck()
    player_hands = {}
    for player in player_list:
        player_hands[player] = deck.deal()
    return player_hands
    

def winner_is(round):
    """Given a dict of players and their hands, determine who the winners are

    Parameter:
    round: dictionary of players and their hands

    Returns:
    returns a string that identifies the round winner(s)
    """
    return hand_evaluator_service.determine_winner(round)


def main():
    """Root of program
    Returns: Ideally nothing if execution wasn't halted by an error in the program
    """
    round = deal_cards(["Johnny", "Timmy", "Jerry", "BARTHOLOMEW"])
    print(winner_is(round))


main()