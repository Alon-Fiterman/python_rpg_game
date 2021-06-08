class Enemy:
    def __init__(self, attack, critical, health, mana):
        self.attack = attack
        self.critical = critical
        self.max_health = health
        self.health = health
        self.max_mana = mana
        self.mana = mana

    def get_attack(self):
        return self.attack

    def get_critical(self):
        return self.critical

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def set_attack(self,new_attack):
        self.attack = new_attack