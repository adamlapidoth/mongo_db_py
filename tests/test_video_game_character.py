def test_attack(player1, player2):
    player1.attack(player2)
    assert player1.energy == 20
    assert player2.health < 50

