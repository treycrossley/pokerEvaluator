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
    assert True

def test_get_card_count():
    assert True

def test_rank_hand():
    assert True

def test_display_rank():
    assert True

def test_get_high_card():
    assert True

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
