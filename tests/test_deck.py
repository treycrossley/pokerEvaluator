from models.deck import Deck


def test_deck():
    deck = Deck()
    assert deck
    assert len(deck.create_deck()) == 52
    assert len(set(deck.create_deck())) == 52
    deckCopy = deck.get_deck()
    assert len(deckCopy) == 52
    deck1 = Deck()
    deck2 = Deck()
    assert deck1 != deck2
    assert deck1.deal(53) == False
    assert len(deck1.deal(10)) == 10
    assert len(deck1.get_deck()) == 42
    assert deck1.num_cards_left() == 42

  