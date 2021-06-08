# while loops
import random

playerhp = 260
my_atk_l = 20
my_atk_h = 50
my_shield = False

enemyhp = 260
enemy_atk_l = 20
enemy_atk_h = 50

while playerhp > 0:

    print("enemy is atacking! defend/attack/potion?", )
    enemy_dmg = random.randrange(enemy_atk_l, enemy_atk_h)
    turn = input()
    if turn == 'defend':
        my_shield = True
        print(enemy_dmg, " Point of damage deflected by your shield")
    elif turn == 'attack':
        my_dmg = random.randrange(my_atk_l, my_atk_h)
        enemyhp = enemyhp - my_dmg
        print("I strike for ", my_dmg, " points of damage! ", " Enemy hp: ", enemyhp)
        playerhp = playerhp - enemy_dmg
        print("Enemy strikes for ", enemy_dmg, " points of damage!", "Current hp: ", playerhp)
    elif turn == 'potion':
        vitality = random.randrange(10, 30)
        playerhp = playerhp + vitality

    if playerhp <= 0:
        playerhp = 0
        print("You have died")
        break
    elif enemyhp <= 0:
        print("enemy is dead")
        break
