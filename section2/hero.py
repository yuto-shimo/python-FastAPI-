from weapon import *

class Hero:
    def __init__(self,health_points,attack_damage):
        self.health_points = health_points
        self.attack_damage = attack_damage
        self.weapon_is_equipped = False
        self.weapon:None

    def equip_weapon(self):
        if self.weapon is not None and not self.weapon_is_equipped:
            self.attack_damage += self.weapon.attack_increase
            self.weapon_is_equipped = True

    def attack(self):
        print(f"Hero attacks for {self.attack_damage} damage")