import random
from utils.background import *


class Character:
    def __init__(self, name, health, mana, attack, defense, magic, items):
        self.name = name
        self.max_health_points = health
        self.health_points = health
        self.max_mana_points = mana
        self.mana_points = mana
        self.regular_attack = attack - 10
        self.critical = attack + 10
        self.defense = defense
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]

    def choose_action(self):
        i = 1
        print("\n" + bcolors.BOLD + self.name + bcolors.ENDC)
        print(bcolors.WARNING + bcolors.BOLD + "    ACTIONS" + bcolors.ENDC)
        for item in self.actions:
            print("       " + str(i) + ":", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "    MAGIC" + bcolors.ENDC)
        for spell in self.magic:
            if spell.type == "white":
                print("       " + str(i) + ".", spell.name, " replenishes:", spell.dmg, "(cost:", str(spell.cost) + ")")
            else:
                print("       " + str(i) + ".", spell.name, " damage:", spell.dmg, "(cost:", str(spell.cost) + ")")
            i += 1

    def choose_item(self):
        i = 1
        print("\n" + bcolors.OKGREEN + bcolors.BOLD + "    ITEMS" + bcolors.ENDC)
        for item in self.items:
            print("       " + str(i) + ".", item["item"].name + ":", item["item"].description,
                  " (x" + str(item["quantity"]) + ")")
            i += 1

    def choose_target(self, enemies):
        i = 1
        print("\n" + bcolors.FAIL + bcolors.BOLD + "    TARGET" + bcolors.ENDC)
        for enemy in enemies:
            if enemy.get_health_points() != 0:
                print("        " + str(i) + ".", enemy.name)
                i += 1
        choice = int(input("    Choose target:")) - 1
        return choice

    def generate_damage(self):
        return random.randrange(self.regular_attack, self.critical)

    def take_damage(self, damage):
        self.health_points -= damage
        if self.health_points < 0:
            self.health_points = 0
            return self.health_points

    def heal(self, damage):
        self.health_points += damage
        if self.health_points > self.max_health_points:
            self.health_points = self.max_health_points

    def reduce_mana_points(self, cost):
        self.mana_points -= cost

    def get_health_points(self):
        return self.health_points

    def get_max_health_points(self):
        return self.max_health_points

    def get_mana(self):
        return self.mana_points

    def get_max_mana(self):
        return self.max_mana_points

    def get_enemy_stats(self):
        hp_bar = ""
        bar_ticks = (self.health_points / self.max_health_points) * 100 / 2

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1
        while len(hp_bar) < 50:
            hp_bar += " "

        # Health points bar space assurance
        hp_string = str(self.health_points) + "/" + str(self.max_health_points)
        current_hp = ""
        if len(hp_string) < 11:
            decreased = 11 - len(hp_string)

            while decreased > 0:
                current_hp += " "
                decreased -= 1
            current_hp += hp_string
        else:
            current_hp = hp_string
    # Stats bar
        print("                   __________________________________________________ ")
        print(bcolors.BOLD + self.name + " " +
              current_hp + " |" + bcolors.FAIL + hp_bar + bcolors.ENDC + bcolors.BOLD + "|")

# Stats Bar
    def get_stats(self):
        hp_bar = ""
        hp_ticks = (self.health_points / self.max_health_points) * 100 / 4
        mp_bar = ""
        mp_tick = (self.mana_points/self.max_mana_points) * 100 / 10
    # Health bar functionality
        while hp_ticks > 0:
            hp_bar += "█"
            hp_ticks -= 1
        while len(hp_bar) < 25:
            hp_bar += " "
    # Mana bar functionality
        while mp_tick > 0:
            mp_bar += "█"
            mp_tick -= 1
        while len(mp_bar) < 10:
            mp_bar += " "
    # Health points bar space assurance
        hp_string = str(self.health_points) + "/" + str(self.max_health_points)
        current_hp = ""
        if len(hp_string) < 9:
            decreased = 9 -len(hp_string)

            while decreased > 0:
                current_hp += " "
                decreased -= 1
            current_hp += hp_string
        else:
            current_hp = hp_string

    # Mana points bar space assurance
        mp_string = str(self.mana_points) + "/" + str(self.max_mana_points)
        current_mp = ""

        if len(mp_string) < 7:
            decreased = 7 - len(mp_string)
            while decreased > 0:
                current_mp += " "
                decreased -= 1
            current_mp += mp_string
        else:
            current_mp = mp_string
        print("                    _________________________             __________ ")
        print(bcolors.BOLD + self.name + "    " +
              current_hp + " |" + bcolors.OKGREEN + hp_bar + bcolors.ENDC + bcolors.BOLD
              + "|   " +
              current_mp + " |" + bcolors.OKBLUE + mp_bar + bcolors.ENDC + "|")

    def choose_enemy_spell(self):
        magic_choice = random.randrange(0, len(self.magic))
        spell = self.magic[magic_choice]
        magic_damage = spell.generate_damage()
        hp_percentage = self.health_points / self.max_health_points * 100

        if self.mana_points < spell.cost or spell.type == "white" and hp_percentage > 50:
            self.choose_enemy_spell()
        else:
            return spell, magic_damage