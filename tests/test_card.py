from models.card import Card
import services.hand_evaluator_service as hand_evaluator_service

def test_card():
    hand = ["10s", "7c", "Ah", "Qd", "2h"]
    for cardStr in hand:
        suit = hand_evaluator_service.get_suit(cardStr)
        value = hand_evaluator_service.get_value(cardStr)
        card = Card(suit,value)
        assert card
        assert card.get_suit() == suit
        assert card.get_value() == value
        c = card.show()
        assert isinstance(c,str)
