from classes.enemy_class import Enemy

warrior = Enemy(10, 30, 200, 100)
print(warrior.get_attack())
warrior.set_attack(100)
print(warrior.get_attack())
