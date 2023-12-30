import copy


def test_attack(player1, player2):
    player1.attack(player2)
    assert player1.energy == 20
    assert player2.health < 50


def test_heal_beyond_max_health(player1, powder):
    assert player1.max_health == 50
    player1.add_item(powder)
    player1.use_item("powder")
    assert player1.max_health == 50


def test_use_item(player2, powder, potion):
    assert powder.quantity == 1
    player2.add_item(powder)
    player2.add_item(potion)
    assert len(player2.items) == 2
    player2.use_item("potion")
    assert len(player2.items) == 1
    assert potion.quantity == 0


def test_add_item(player1, potion, powder):
    player1.add_item(potion)
    player1.add_item(powder)
    assert len(player1.items) == 2


def test_stat(player2, potion):
    expected = copy.deepcopy(vars(player2))
    expected["items"].append(copy.deepcopy(vars(potion)))
    player2.add_item(potion)
    assert player2.stat() == expected


def test_player_eq(player2, potion):
    assert player2 != potion
