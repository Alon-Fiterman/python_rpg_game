import random

class Spell:
    def __init__(self, name, cost, dmg, type):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.type = type

    def generate_damage(self):
        low_strike = self.dmg - 15
        high_strike = self.dmg + 15
        return random.randrange(low_strike,high_strike)