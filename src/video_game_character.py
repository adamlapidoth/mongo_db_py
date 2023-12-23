import copy


class Player:
    def __init__(self, name, max_health, max_energy, items=None):
        if items is None:
            items = []
        self.name = name
        self.health = max_health,
        self.energy = max_energy,
        self.items = copy.deepcopy(items)

    def attack(self, player: Player):
        energy_cost = 5

        if self.energy >= energy_cost:
            pass
        else:
            print(
                f"{self.name} does not have enough energy to attack {player.name}")
