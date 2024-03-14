import services.hand_evaluator_service as hand_evaluator_service
import pytest

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
    players_info = [
        ["Doc Marten", ["10s", "10c", "4h", "10d", "10h"], 7],
        ["Katy Perry", ["6s", "6c", "4h", "6d", "6h"], 7],
        ["Austin Powers", ["4s", "4c", "4h", "4d", "10h"], 7],
        ["Trey Crossley", ["4s", "3c", "Kh", "8d", "10h"], 0],
    ]
    grouped = hand_evaluator_service.group_by_rank(players_info)
    assert len(grouped[7]) == 3

def test_compare_straight_flush():
    players_info = [
        ["Doc Marten", ["10s", "Js", "Qs", "Ks", "9s"]],
        ["Katy Perry", ["10c", "9c", "8c", "7c", "6c"]],
        ["Austin Powers", ["4s", "3s", "5s", "6s", "7s"]],
        ["Trey Crossley", ["7h", "9h", "Jh", "8h", "10h"]],
    ]
    competitors = hand_evaluator_service.compare_straight_flush(players_info)
    d = {}
    for competitor in competitors:
        name = competitor[0]
        rank = competitor[2]
        d[name] = rank
    assert d["Doc Marten"] > d["Trey Crossley"] > d["Katy Perry"] > d["Austin Powers"]

def test_compare_4kind():
    players_info = [
        ["Doc Marten", ["10s", "10c", "10d", "10h", "9s"]],
        ["Katy Perry", ["10c", "6s", "6h", "6d", "6c"]],
        ["Austin Powers", ["4s", "4h", "4d", "4c", "7s"]],
        ["Trey Crossley", ["8h", "8s", "8c", "8d", "10h"]],
    ]
    competitors = hand_evaluator_service.compare_4kind(players_info)
    d = {}
    for competitor in competitors:
        name = competitor[0]
        rank = competitor[2]
        d[name] = rank
    assert d["Doc Marten"] > d["Trey Crossley"] > d["Katy Perry"] > d["Austin Powers"]


def test_compare_full_house():
    players_info = [
        ["Doc Marten", ["10s", "10c", "10d", "9h", "9s"]],
        ["Katy Perry", ["3c", "3s", "3h", "2d", "2c"]],
        ["Austin Powers", ["3s", "3h", "2d", "2c", "2s"]],
        ["Trey Crossley", ["10h", "8s", "8c", "8d", "10c"]],
    ]
    competitors = hand_evaluator_service.compare_full_house(players_info)
    d = {}
    for competitor in competitors:
        name = competitor[0]
        rank = competitor[2]
        d[name] = rank
    assert d["Doc Marten"] > d["Trey Crossley"] > d["Katy Perry"] > d["Austin Powers"]



def test_compare_flush():
    players_info = [
        ["Doc Marten", ["8s", "2s", "5s", "9s", "As"]],
        ["Katy Perry", ["Jc", "3c", "7c", "2c", "2c"]],
        ["Austin Powers", ["5h", "3h", "2h", "8h", "7h"]],
        ["Trey Crossley", ["2c", "5c", "Qc", "8c", "10c"]],
    ]
    competitors = hand_evaluator_service.compare_flush(players_info)
    d = {}
    for competitor in competitors:
        name = competitor[0]
        rank = competitor[2]
        d[name] = rank
    assert d["Doc Marten"] > d["Trey Crossley"] > d["Katy Perry"] > d["Austin Powers"]



def test_compare_straight():
    players_info = [
        ["Doc Marten", ["Kc", "Js", "Qh", "10s", "9d"]],
        ["Katy Perry", ["Jc", "10d", "9s", "8c", "7c"]],
        ["Austin Powers", ["Ac", "2s", "3h", "4s", "5d"]],
        ["Trey Crossley", ["8d", "10c", "Qc", "Jh", "9s"]],
    ]
    competitors = hand_evaluator_service.compare_straight(players_info)
    d = {}
    for competitor in competitors:
        name = competitor[0]
        rank = competitor[2]
        d[name] = rank
    assert d["Doc Marten"] > d["Trey Crossley"] > d["Katy Perry"] > d["Austin Powers"]



def test_compare_3kind():
    players_info = [
        ["Doc Marten", ["Ac", "As", "Ah", "10s", "9d"]],
        ["Katy Perry", ["Jc", "7d", "9s", "7s", "7c"]],
        ["Austin Powers", ["2c", "2s", "2h", "4s", "5d"]],
        ["Trey Crossley", ["10d", "10c", "Qc", "10h", "9s"]],
    ]
    competitors = hand_evaluator_service.compare_3kind(players_info)
    d = {}
    for competitor in competitors:
        name = competitor[0]
        rank = competitor[2]
        d[name] = rank
    assert d["Doc Marten"] > d["Trey Crossley"] > d["Katy Perry"] > d["Austin Powers"]


def test_filter_hand():
    assert hand_evaluator_service.filter_hand(["10s", "10c", "4h", "10d", "10h"], 10) == ["4h"]
    assert hand_evaluator_service.filter_hand(["10s", "2c", "4h", "2d", "7h"], 8) == ["10s", "2c", "4h", "2d", "7h"]
    assert hand_evaluator_service.filter_hand(["10s", "2c", "4h", "2d", "7h"], 2) == ["10s", "4h", "7h"]

def test_compare_2pair():
    players_info = [
        ["Doc Marten", ["Ac", "As", "10h", "10s", "9d"]],
        ["Katy Perry", ["Ac", "Ad", "8s", "9s", "9c"]],
        ["Austin Powers", ["2c", "2s", "3h", "3s", "4d"]],
        ["Trey Crossley", ["10d", "10c", "Ac", "Ah", "8s"]],
    ]
    competitors = hand_evaluator_service.compare_2pair(players_info)
    d = {}
    for competitor in competitors:
        name = competitor[0]
        rank = competitor[2]
        d[name] = rank
    assert d["Doc Marten"] > d["Trey Crossley"] > d["Katy Perry"] > d["Austin Powers"]

def test_compare_pair():
    players_info = [
        ["Doc Marten", ["Ac", "As", "9h", "10s", "8d"]],
        ["Katy Perry", ["7c", "7d", "8s", "2s", "9c"]],
        ["Austin Powers", ["2c", "As", "3h", "3s", "4d"]],
        ["Trey Crossley", ["10d", "10c", "6c", "Ah", "8s"]],
    ]
    competitors = hand_evaluator_service.compare_pair(players_info)
    d = {}
    for competitor in competitors:
        name = competitor[0]
        rank = competitor[2]
        d[name] = rank
    assert d["Doc Marten"] > d["Trey Crossley"] > d["Katy Perry"] > d["Austin Powers"]


def test_compare_high_card():
    players_info = [
        ["Doc Marten", ["Ac", "7s", "3h", "10s", "8d"]],
        ["Katy Perry", ["7c", "4d", "8s", "2s", "9c"]],
        ["Austin Powers", ["2c", "5s", "3h", "3s", "6d"]],
        ["Trey Crossley", ["10d", "10c", "6c", "Qh", "8s"]],
    ]
    competitors = hand_evaluator_service.compare_high_card(players_info)
    d = {}
    for competitor in competitors:
        name = competitor[0]
        rank = competitor[2]
        d[name] = rank
    assert d["Doc Marten"] > d["Trey Crossley"] > d["Katy Perry"] > d["Austin Powers"]


# @mock.patch("services.hand_evaluator_service.eval_tie", return_value = 5, autospec=True)
def test_eval_tie():
    returnVal = hand_evaluator_service.eval_tie(0, []) 
    assert isinstance(returnVal, list)
    returnVal = hand_evaluator_service.eval_tie(1, []) 
    assert isinstance(returnVal, list)
    returnVal = hand_evaluator_service.eval_tie(2, []) 
    assert isinstance(returnVal, list)
    returnVal = hand_evaluator_service.eval_tie(3, []) 
    assert isinstance(returnVal, list)
    returnVal = hand_evaluator_service.eval_tie(4, []) 
    assert isinstance(returnVal, list)
    returnVal = hand_evaluator_service.eval_tie(5, []) 
    assert isinstance(returnVal, list)
    returnVal = hand_evaluator_service.eval_tie(6, []) 
    assert isinstance(returnVal, list)
    returnVal = hand_evaluator_service.eval_tie(7, []) 
    assert isinstance(returnVal, list)
    returnVal = hand_evaluator_service.eval_tie(8, []) 
    assert isinstance(returnVal, list)
    returnVal = hand_evaluator_service.eval_tie(9, []) 
    assert isinstance(returnVal, list)





def test_eval_tiebreakers():
    players_info = [
        ["Doc Marten", ["Ac", "7s", "3h", "10s", "8d"], 0],
        ["Katy Perry", ["7c", "4d", "8s", "2s", "9c"], 0],
        ["Austin Powers", ["2c", "5s", "3h", "3s", "6d"], 0],
        ["Trey Crossley", ["10d", "10c", "6c", "Qh", "8s"], 0],
    ]
    competitors = hand_evaluator_service.eval_tiebreakers(players_info)
    d = {}
    for competitor in competitors:
        name = competitor[0]
        rank = competitor[2]
        d[name] = rank
    assert d["Doc Marten"] > 0
    assert d["Trey Crossley"] > 0
    assert d["Katy Perry"] > 0 
    assert d["Austin Powers"] > 0
    assert d["Doc Marten"] > d["Trey Crossley"] > d["Katy Perry"] > d["Austin Powers"]

def test_determine_player_rankings():
    players_info = {
        "Doc Marten": ["10c", "Jc", "Qc", "Ac", "Kc"],
        "Katy Perry": ["7c", "4d", "8s", "7s", "2c"],
        "Austin Powers": ["3h", "5h", "Qs", "9h", "Ac"],
        "Trey Crossley": ["10s", "10c", "Ah", "10d", "10h"]
    }
    competitors = hand_evaluator_service.determine_player_rankings(players_info)
    d = {}
    for competitor in competitors:
        name = competitor[0]
        rank = competitor[2]
        d[name] = rank
    assert d["Doc Marten"] >= 9
    assert d["Trey Crossley"] >= 7 and d["Trey Crossley"] < 8
    assert d["Katy Perry"] >= 1 and d["Katy Perry"] < 2
    assert d["Austin Powers"] >= 0 and d["Austin Powers"] < 1
    assert d["Doc Marten"] > d["Trey Crossley"] > d["Katy Perry"] > d["Austin Powers"]


def test_determine_winner():
    players_info = {
        "Doc Marten": ["10c", "Jc", "Qc", "Ac", "Kc"],
        "Katy Perry": ["7c", "4d", "8s", "7s", "2c"],
        "Austin Powers": ["3h", "5h", "Qs", "9h", "Ac"],
        "Trey Crossley": ["10s", "10c", "Ah", "10d", "10h"]
    }
    winner = hand_evaluator_service.determine_winner(players_info)
    assert winner == "Doc Marten"
