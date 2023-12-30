from __future__ import (
    annotations,
)  # need this to type hint Player from the method attack

import copy

import numpy as np


class Player:
    def __init__(self, name, max_health, max_energy, items=None):
        if items is None:
            items = []
        self.name = name
        self.health = max_health
        self.max_health = max_health
        self.energy = max_energy
        self.max_energy = max_energy
        self.items = copy.deepcopy(items)

    def attack(self, player: Player):
        energy_cost = 5

        if self.energy >= energy_cost:
            rng = np.random.default_rng(42)
            attack_strength = rng.integers(1, 6)
            player.health -= attack_strength
            self.energy -= energy_cost
            print(f"{self.name} attacked {player.name} for {attack_strength} damage")
        else:
            print(f"{self.name} does not have enough energy to attack {player.name}")

    def heal(self, amount: int):
        self.health += amount

        if self.health > self.max_health:
            self.health = self.max_health

    def stat(self):
        return vars(self)

    def use_item(self, item_name):
        try:
            item = next(item for item in self.items if item.name == item_name)
            item.quantity -= 1

            for effect in item.effects:
                for method, value in effect.items():
                    class_method = getattr(self, method)
                    class_method(value)

            if item.quantity == 0:
                self.items.remove(item)

        except AttributeError:
            print(f"{self.name} does not have any {item_name}s")

    def add_item(self, item):
        self.items.append(item)

    def __eq__(self, other: Player):
        if not isinstance(other, Player):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return (
            self.name == other.name
            and self.max_health == other.max_health
            and self.health == other.health
            and self.max_energy == other.max_energy
            and self.energy == other.energy
            and self.items == other.items
        )


class Item:
    def __init__(self, name, quantity, effects=None):
        if effects is None:
            effects = []
        self.name = name
        self.quantity = quantity
        self.effects = effects

    def __repr__(self):
        return (
            f"{self.__class__.__name__}(name={self.name}, quantity={self.quantity},"
            f" effects={self.effects}"
        )

    def __eq__(self, other: Item):
        if not isinstance(other, Item):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return (
            self.name == other.name
            and self.quantity == other.quantity
            and self.effects == other.effects
        )

    def stat(self):
        return vars(self)
