from models.deck import Deck

def test_deck_init():
    deck = Deck()
    assert deck
    assert len(deck.create_deck()) == 52
    assert len(set(deck.create_deck())) == 52

def test_deck_getter():
    deck = Deck()
    deckCopy = deck.get_deck()
    assert len(deckCopy) == 52

def test_shuffled():
    deck1 = Deck()
    deck2 = Deck()
    assert deck1 != deck2

def test_deal():
    deck = Deck()
    assert len(deck.deal(10)) == 10
    assert len(deck.get_deck()) == 42
    assert deck.num_cards_left() == 42
  