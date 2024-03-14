from card import Card
import hand_evaluator_service

test_hands = [
    ["Ac", "5c", "10c", "7c", "3s"],
    ["2c", "3d", "4s", "5h", "2d"],
    ["2c", "3d", "4s", "3h", "2d"],
    ["5s", "4c", "Ad", "4s", "4h"],
    ["3h", "7h", "6s", "4d", "5s"],
    ["Ac", "5c", "10c", "7c", "3c"],
    ["5c", "8d", "5h", "8s", "8h"],
    ["3d", "7h", "7s", "7c", "7d"],
    ["As", "10s", "Qs", "Ks", "Js"],
]


# Part 1
def hand_ranking(hand=[]):
    print()
    print("Is flush: {}".format(hand_evaluator_service.is_flush(hand)))
    return "hand"

# Part 2
def deal_cards(player_list):
    """doc"""
    pass

def winner_is(round):
    """doc"""
    pass



def main():
    for hand in test_hands:
        print(hand_ranking(hand))


main()