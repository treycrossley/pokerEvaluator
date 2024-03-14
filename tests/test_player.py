from models.player import Player
from models.deck import Deck
import pytest

def test_player_init():
    deck = Deck()
    player = Player("Smitty Warbenjaegermanjenson", deck)
    assert player
    assert not player.hand

def test_draw_cards():
    deck = Deck()
    player = Player("danny", deck)
    player.draw_cards(5)
    assert len(player.hand) == 5
    assert player.draw_cards(400) is False
    assert len(player.hand) == 5


def test_show_hand():
    deck = Deck()
    player = Player("billy", deck)
    assert isinstance(player.show_hand(),str)