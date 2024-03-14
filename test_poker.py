import poker

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

def test_hand_ranking():
    assert poker.hand_ranking(["10c", "Jc", "Qc", "Ac", "Kc"]) == "Royal Flush"
    assert poker.hand_ranking(["3h", "5h", "Qs", "9h", "Ac"]) == "High Card"
    assert poker.hand_ranking(["10s", "10c", "Ah", "10d", "10h"]) == "Four of a Kind"

def test_deal_cards():
    result = poker.deal_cards(["Westley","Buttercup"])
    assert len(result["Westley"]) == 5
    assert len(result["Buttercup"]) == 5
    bothHands = result["Buttercup"] + result["Westley"]
    assert len(set(bothHands)) == 10

def test_winner_is():
    round_1 = {"Inigo" : ["10h", "Jh", "Qh", "Ah", "Kh"], 
        "Fezzik" : ["3h", "5h", "Qs", "9h", "Ad"]}
    assert poker.winner_is(round_1) == "Inigo"

