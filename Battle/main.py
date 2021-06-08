import random
from classes.game import *
from utils.background import *
from classes.magic import *
from classes.inventory import *

# Create Black Magic
fire = Spell("Fire", 20, 500, "black")
thunder = Spell("Thunder", 25, 600, "black")
blizzard = Spell("Blizzard", 23, 550, "black")
meteor = Spell("Meteor", 40, 850, "black")
quake = Spell("Quake", 12, 340, "black")

# Create White Magic
cure = Spell("Cure", 20, 900, "white")
cura = Spell("Cura", 50, 3500, "white")

# Create some items
small_health_potion = Item("Small Potion", "potion", "heals 50 HP", 50)
big_health_potion = Item("Big Potion", "potion", "Heals 100 HP", 100)
super_potion = Item("Super potion", "potion", "Heals 1000 HP", 1000)
elixir = Item("Elixir", "elixir", "Fully restores HP/MP of one party member", 9999)
mega_elixir = Item("Mega elixir", "elixir", "Fully restores party's HP/MP", 9999)
grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, cure, cura]
enemy_spells =  [fire, meteor, cura]

player_items = [{"item": small_health_potion, "quantity": 10},
                {"item": big_health_potion, "quantity": 4},
                {"item": super_potion, "quantity": 3},
                {"item": elixir, "quantity": 2},
                {"item": mega_elixir, "quantity": 1},
                {"item": grenade, "quantity": 3}]

# Instantiate People
player_1 = Character("Valos", 3460, 132, 301, 34, player_spells, player_items)
player_2 = Character("Firye", 4460, 188, 290, 34, player_spells, player_items)
player_3 = Character("Ramos", 3460, 174, 300, 34, player_spells, player_items)

enemy_1 = Character("Robot", 5500, 135, 560, 325, enemy_spells, [])
enemy_2 = Character("Magus", 12200, 150, 525, 25, enemy_spells, [])
enemy_3 = Character("Robot", 5500, 135, 560, 325, enemy_spells, [])

players = [player_1, player_2, player_3]
enemies = [enemy_1, enemy_2, enemy_3]

running = True
i = 0
print(bcolors.FAIL + bcolors.BOLD + "WARNING /\(◣_◢)/\o=}======> AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("========================================================================")
    print("NAME                 HEALTH                                MANA ")

    for enemy in enemies:
        enemy.get_enemy_stats()
    print("\n")
    for player in players:
        player.get_stats()
    for player in players:
        player.choose_action()
        choice = input("    Choose action: ")
        index = int(choice) - 1

        # Normal Attack
        if index == 0:
            damage = player.generate_damage()
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(damage)
            print(bcolors.OKGREEN + bcolors.BOLD, player.name + bcolors.ENDC,
                  "attacks " + bcolors.FAIL + bcolors.BOLD + enemies[
                      enemy].name.replace(" ", ""), bcolors.ENDC + " for ", bcolors.WARNING, damage, bcolors.ENDC,
                  "points of damage.")
            # fixes after death list number problem ==> del
            if enemies[enemy].get_health_points() == 0:
                print(bcolors.WARNING + bcolors.BOLD, enemies[enemy].name.replace(" ", "") + " has been defeated",
                      bcolors.ENDC)
                del enemies[enemy]
        # Picks Magic
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("Choose magic: ")) - 1

            # Previous menu
            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            spell_damage = spell.generate_damage()
            current_mana = player.get_mana()
            cost = spell.cost

            if spell.cost > current_mana:
                print(bcolors.FAIL + "\nNot enough Mana points\n" + bcolors.ENDC)
                continue
            player.reduce_mana_points(spell.cost)

            if spell.type == "white":
                player.heal(spell_damage)
                print(bcolors.OKBLUE + "\n" + spell.name + " replenished", str(spell_damage), "health" + bcolors.ENDC)
            elif spell.type == "black":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(spell_damage)
                print(bcolors.OKBLUE + bcolors.BOLD + "\n" + spell.name + " deals", str(spell_damage),
                      "points of damage to " + enemies[enemy].name.replace(" ", "") + bcolors.ENDC)
                # fixes after death list number problem ==> del
                if enemies[enemy].get_health_points() == 0:
                    print(bcolors.WARNING + bcolors.BOLD, enemies[enemy].name.replace(" ", "") + " has been defeated",
                          bcolors.ENDC)
                    del enemies[enemy]
        # Items pick
        elif index == 2:
            player.choose_item()
            item_choice = int(input("Choose item: ")) - 1
            item = player.items[item_choice]["item"]
            if player.items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL + "\n" + "None left...", bcolors.ENDC)
                continue
            player.items[item_choice]["quantity"] -= 1

            # this line of code makes it possible to return to previous menu, out of the loop
            if item_choice == -1:
                continue

            if item.type == "potion":
                player.heal(item.properties)
                print(bcolors.OKGREEN + "\n" + item.name + " replenished", str(item.properties), "HP" + bcolors.ENDC)
            elif item.type == "elixir":
                if item.name == "Mega elixir":
                    for i in players:
                        i.health_points = i.max_health_points
                        i.mana_points = i.max_mana_points
                else:
                    player.health_points = player.max_health_points
                    player.mana_points = player.max_mana_points
                print(bcolors.OKGREEN + "\n" + item.name + " fully restored health and mana" + bcolors.ENDC)
            elif item.type == "attack":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item.properties)
                print(bcolors.FAIL + "\n" + item.name + " dealt", str(item.properties) + " points of damage to ",
                      bcolors.ENDC)
                # fixes after death list number problem ==> del
                if enemies[enemy].get_health_points() == 0:
                    print(bcolors.WARNING + bcolors.BOLD,
                          enemies[enemy].name.replace(" ", "") + " has been defeated", bcolors.ENDC)
                    del enemies[enemy]
    # Check if battle is over
    defeated_enemies = 0
    defeated_players = 0

    for enemy in enemies:
        if enemy.get_health_points() == 0:
            defeated_enemies += 1
    for player in players:
        if player.get_health_points() == 0:
            defeated_players += 1
    # Check if player won
    if defeated_enemies == 3:
        print("\n" + bcolors.OKGREEN + "(}o{≧O≦}o]====> GLORIOUS VICTORY !!!" + bcolors.ENDC)
        running = False
    # Check if enemy won
    elif defeated_players == 3:
        print(bcolors.FAIL, "(✖╭╮✖) THE ENEMY IS VICTORIOUS (✖╭╮✖)", bcolors.ENDC)
        running = False
    print("\n")

    # Enemy attacking mechanism
    for enemy in enemies:
        enemy_choice = random.randrange(0, 2)
        if enemy_choice == 0:
            # Choose type of attack
            target = random.randrange(0, 3)
            enemy_damage = enemy.generate_damage()
            players[target].take_damage(enemy_damage)
            print(" " + bcolors.FAIL + bcolors.BOLD + enemy.name.replace(" ", "") + bcolors.ENDC +
                  " attacks " + bcolors.OKGREEN + players[target].name.replace(" ", ""), bcolors.ENDC +
                  " for ", bcolors.WARNING, enemy_damage, bcolors.ENDC,
                  "points of damage.")
        elif enemy_choice == 1:
            spell, magic_damage = enemy.choose_enemy_spell()
            enemy.reduce_mana_points(spell.cost)
            if spell.type == "white":
                enemy.heal(magic_damage)
                print(" " + bcolors.OKBLUE + bcolors.BOLD + spell.name + " heals " + enemy.name + " for", str(magic_damage),
                      "health" + bcolors.ENDC)
            elif spell.type == "black":
                target = random.randrange(0, 3)
                players[target].take_damage(magic_damage)
                print(" " + bcolors.OKBLUE + bcolors.BOLD + enemy.name.replace(" ", "") + "'s " + spell.name + " deals",
                    str(magic_damage), "points of damage to " + players[target].name.replace(" ", "") + bcolors.ENDC)
                # fixes after death list number problem ==> del
                if players[target].get_health_points() == 0:
                    print(bcolors.WARNING + bcolors.BOLD, players[target].name.replace(" ", "") + " has been defeated",
                          bcolors.ENDC)
                    del players[target]
            # print("Enemy chose", spell, "damage is", magic_damage)
