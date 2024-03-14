from models.deck import Deck
from models.card import Card
import services.hand_evaluator_service as hand_evaluator_service

test_hands = [
    ["Ac", "5c", "10c", "7c", "3s"],
    ["2c", "3d", "4s", "5h", "2d"],
    ["2c", "3d", "4s", "3h", "2d"],
    ["5s", "4c", "Ad", "4s", "4h"],
    ["3h", "7h", "6s", "4d", "5s"],
    ["Ac", "5c", "10c", "7c", "3c"],
    ["5c", "8d", "5h", "8s", "8h"],
    ["3d", "7h", "7s", "7c", "7d"],
    ["5c", "4c", "8c", "7c", "6c"],
    ["As", "10s", "Qs", "Ks", "Js"],
    ["10c", "Jc", "Qc", "Ac", "Kc"],
    ["3h", "5h", "Qs", "9h", "Ac"],
    ["10s", "10c", "Ah", "10d", "10h"]
]

test_players = ["Westley", "Buttercup", "Inigo", "Fezzik"]

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
    round = deal_cards(test_players)
    print(winner_is(round))


main()