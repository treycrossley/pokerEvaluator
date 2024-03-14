import services.hand_evaluator_service as hand_evaluator_service

def test_get_suit():
    assert hand_evaluator_service.get_suit("Qs") == "s"
    assert hand_evaluator_service.get_suit("10c") == "c"
    assert hand_evaluator_service.get_suit("Ah") == "h"
    assert hand_evaluator_service.get_suit("7s") == "s"
    assert hand_evaluator_service.get_suit("4d") == "d"

def test_get_value():
    assert hand_evaluator_service.get_value("Qs") == 12
    assert hand_evaluator_service.get_value("10c") == 10
    assert hand_evaluator_service.get_value("Ah") == 14
    assert hand_evaluator_service.get_value("7s") == 7
    assert hand_evaluator_service.get_value("4d") == 4

def test_is_flush():
    assert not hand_evaluator_service.is_flush(["Ac", "5c", "10c", "7c", "3s"])
    assert not hand_evaluator_service.is_flush(["2c", "3d", "4s", "5h", "2d"])
    assert not hand_evaluator_service.is_flush(["2c", "3d", "4s", "3h", "2d"])
    assert not hand_evaluator_service.is_flush(["5s", "4c", "Ad", "4s", "4h"])
    assert not hand_evaluator_service.is_flush(["3h", "7h", "6s", "4d", "5s"])
    assert hand_evaluator_service.is_flush(["Ac", "5c", "10c", "7c", "3c"])
    assert not hand_evaluator_service.is_flush(["5c", "8d", "5h", "8s", "8h"])
    assert not hand_evaluator_service.is_flush(["3d", "7h", "7s", "7c", "7d"])
    assert hand_evaluator_service.is_flush(["5c", "4c", "8c", "7c", "6c"])
    assert hand_evaluator_service.is_flush(["As", "10s", "Qs", "Ks", "Js"])
    assert hand_evaluator_service.is_flush(["10c", "Jc", "Qc", "Ac", "Kc"])
    assert not hand_evaluator_service.is_flush(["3h", "5h", "Qs", "9h", "Ac"],)
    assert not hand_evaluator_service.is_flush(["10s", "10c", "Ah", "10d", "10h"])


def test_get_card_frequency():
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

    for hand in test_hands:
        freq = hand_evaluator_service.get_card_frequency(hand)
        res = sum(freq.values())
        if any( hand_evaluator_service.get_value(card) == 14  for card in hand):
            res -= 1
        assert res == 5


def test_get_straight_high_card():
    assert hand_evaluator_service.get_straight_high_card(["Ac", "5c", "10c", "7c", "3s"]) is None
    assert hand_evaluator_service.get_straight_high_card(["2c", "3d", "4s", "5h", "2d"]) is None
    assert hand_evaluator_service.get_straight_high_card(["2c", "3d", "4s", "3h", "2d"]) is None
    assert hand_evaluator_service.get_straight_high_card(["5s", "4c", "Ad", "4s", "4h"]) is None
    assert hand_evaluator_service.get_straight_high_card(["3h", "7h", "6s", "4d", "5s"]) is 7
    assert hand_evaluator_service.get_straight_high_card(["Ac", "5c", "10c", "7c", "3c"]) is None
    assert hand_evaluator_service.get_straight_high_card(["Ac", "3d", "2h", "4s", "5h"]) is 5
    assert hand_evaluator_service.get_straight_high_card(["3d", "7h", "7s", "7c", "7d"]) is None
    assert hand_evaluator_service.get_straight_high_card(["5c", "4c", "8c", "7c", "6c"]) is 8
    assert hand_evaluator_service.get_straight_high_card(["As", "10s", "Qs", "Ks", "Js"]) is 14
    assert hand_evaluator_service.get_straight_high_card(["10c", "Jc", "Qc", "Ac", "Kc"]) is 14
    assert hand_evaluator_service.get_straight_high_card(["3h", "5h", "Qs", "9h", "Ac"],) is None
    assert hand_evaluator_service.get_straight_high_card(["10s", "10c", "Ah", "10d", "10h"]) is None

def test_get_card_count():
    assert hand_evaluator_service.get_card_count(["Ac", "5c", "10c", "7c", "3s"],3) is None
    assert hand_evaluator_service.get_card_count(["2c", "3d", "4s", "5h", "2d"], 2) is 2
    assert hand_evaluator_service.get_card_count(["2c", "3d", "4s", "3h", "2d"],2) is 2
    assert hand_evaluator_service.get_card_count(["2c", "3d", "4s", "3h", "2d"],2,2) is 3
    assert hand_evaluator_service.get_card_count(["5s", "4c", "Ad", "4s", "4h"],3) is 4
    assert hand_evaluator_service.get_card_count(["3h", "7h", "6s", "4d", "5s"],2) is None
    assert hand_evaluator_service.get_card_count(["Ac", "5c", "10c", "7c", "3c"],4) is None
    assert hand_evaluator_service.get_card_count(["Ac", "3d", "2h", "4s", "5h"],4) is None
    assert hand_evaluator_service.get_card_count(["3d", "7h", "7s", "7c", "7d"],4) is 7
    assert hand_evaluator_service.get_card_count(["5c", "4c", "8c", "7c", "6c"],2) is None
    assert hand_evaluator_service.get_card_count(["As", "10s", "Qs", "Qc", "Qh"],3) is 12
    assert hand_evaluator_service.get_card_count(["10c", "Jc", "Jc", "Jc", "Jc"],4) is 11
    assert hand_evaluator_service.get_card_count(["3h", "5h", "Qs", "9h", "Ac"],2) is None
    assert hand_evaluator_service.get_card_count(["10s", "10c", "Ah", "10d", "10h"], 4) is 10

def test_rank_hand():
    test_hands = [
    ["AC", "5C", "10C", "7C", "3S"],
    ["2C", "3D", "4S", "5H", "2D"],
    ["2C", "3D", "4S", "3H", "2D"],
    ["5S", "4C", "AD", "4S", "4H"],
    ["3H", "7H", "6S", "4D", "5S"],
    ["AC", "5C", "10C", "7C", "3C"],
    ["5C", "8D", "5H", "8S", "8H"],
    ["3D", "7H", "7S", "7C", "7D"],
    ["AS", "10S", "QS", "KS", "JS"],
]
    assert hand_evaluator_service.rank_hand(["AS", "10S", "QS", "KS", "JS"]) == 9
    assert hand_evaluator_service.rank_hand(["3D", "7H", "7S", "7C", "7D"]) == 7
    assert hand_evaluator_service.rank_hand(["5C", "4C", "6C", "7C", "8C"]) == 8
    assert hand_evaluator_service.rank_hand(["AC", "5C", "10C", "7C", "3C"]) == 5
    assert hand_evaluator_service.rank_hand(["3H", "7H", "6S", "4D", "5S"]) == 4
    assert hand_evaluator_service.rank_hand(["5S", "4C", "AD", "4S", "4H"]) == 3
    assert hand_evaluator_service.rank_hand(["5C", "8D", "5H", "8S", "8H"]) == 6
    assert hand_evaluator_service.rank_hand(["2C", "3D", "4S", "3H", "2D"]) == 2
    assert hand_evaluator_service.rank_hand(["AC", "5C", "10C", "7C", "3S"]) == 0
    assert hand_evaluator_service.rank_hand(["2C", "3D", "4S", "5H", "2D"]) == 1

def test_display_rank():
    assert hand_evaluator_service.display_rank(9) == "Royal Flush"
    assert hand_evaluator_service.display_rank(8) == "Straight Flush"
    assert hand_evaluator_service.display_rank(7) == "Four of a Kind"
    assert hand_evaluator_service.display_rank(6) == "Full House"
    assert hand_evaluator_service.display_rank(4) == "Straight"
    assert hand_evaluator_service.display_rank(5) == "Flush"
    assert hand_evaluator_service.display_rank(3) == "Three of a Kind"
    assert hand_evaluator_service.display_rank(2) == "Two Pair"
    assert hand_evaluator_service.display_rank(1) == "Pair"
    assert hand_evaluator_service.display_rank(0) == "High Card"

def test_get_high_card():
    assert hand_evaluator_service.get_high_card(["Ac", "5c", "10c", "7c", "3s"]) is 14
    assert hand_evaluator_service.get_high_card(["2c", "3d", "4s", "5h", "2d"]) is 5
    assert hand_evaluator_service.get_high_card(["2c", "3d", "4s", "3h", "2d"]) is 4
    assert hand_evaluator_service.get_high_card(["5s", "4c", "Ad", "4s", "4h"]) is 14
    assert hand_evaluator_service.get_high_card(["3h", "7h", "6s", "4d", "5s"]) is 7
    assert hand_evaluator_service.get_high_card(["Jc", "5c", "10c", "7c", "3c"]) is 11
    assert hand_evaluator_service.get_high_card(["Ac", "3d", "2h", "4s", "5h"]) is 14
    assert hand_evaluator_service.get_high_card(["3d", "7h", "7s", "7c", "7d"]) is 7
    assert hand_evaluator_service.get_high_card(["5c", "4c", "8c", "7c", "6c"]) is 8
    assert hand_evaluator_service.get_high_card(["Kc", "10s", "Qs", "Ks", "Js"]) is 13
    assert hand_evaluator_service.get_high_card(["10c", "Jc", "Qc", "Ac", "Kc"]) is 14
    assert hand_evaluator_service.get_high_card(["3h", "5h", "Qs", "9h", "Qc"],) is 12
    assert hand_evaluator_service.get_high_card(["10s", "10c", "4h", "10d", "10h"]) is 10

def test_group_by_rank():
    assert True

def test_compare_straight_flush():
    assert True

def test_compare_4kind():
    assert True


def test_compare_full_house():
    assert True


def test_compare_flush():
    assert True

def test_compare_straight():
    assert True

def test_compare_3kind():
    assert True

def test_filter_hand():
    assert True

def test_compare_2pair():
    assert True

def test_compare_pair():
    assert True

def test_compare_high_card():
    assert True

def test_eval_tie():
    assert True

def test_eval_tiebreakers():
    assert True

def determine_player_rankings():
    assert True

def determine_winner():
    assert True
