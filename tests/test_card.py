from models.card import Card
import services.hand_evaluator_service as hand_evaluator_service

hand = ["10s", "7c", "Ah", "Qd", "2h"]

def test_card_init():
    for cardStr in hand:
        suit = hand_evaluator_service.get_suit(cardStr)
        value = hand_evaluator_service.get_value(cardStr)
        card = Card(suit,value)
        assert card

def test_card_getters():
    for cardStr in hand:
        suit = hand_evaluator_service.get_suit(cardStr)
        value = hand_evaluator_service.get_value(cardStr)
        card = Card(suit,value)
        assert card.get_suit() == suit
        assert card.get_value() == value

def test_card_show():
     for cardStr in hand:
        suit = hand_evaluator_service.get_suit(cardStr)
        value = hand_evaluator_service.get_value(cardStr)
        card = Card(suit,value)
        c = card.show()
        assert isinstance(c,str)