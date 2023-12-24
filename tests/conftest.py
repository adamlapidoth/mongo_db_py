import pytest

from video_game_character import Player, Item


@pytest.fixture
def player1():
    return Player(name="player1", max_health=50, max_energy=25)


@pytest.fixture
def player2():
    return Player(name="player2", max_health=50, max_energy=25)


@pytest.fixture
def potion():
    return Item(name="potion", quantity=1, effects=[{"heal": 20}])


@pytest.fixture
def powder():
    return Item(name="powder", quantity=1, effects=[{"heal": 10}])
