class Enemy:

    def __init__(self,type_of_enemy,health_points = 10,attack_damage = 2):
        self.__type_of_enemy: str = type_of_enemy
        self.health_points: int = health_points
        self.attack_damage: int = attack_damage

    def talk(self):
        print(f'i am a {self.__type_of_enemy}. Be prepared to fight! ')

    def wslk_forward(self):
        print(f'{self.__type_of_enemy} moves closer to you.')

    def attack(self):
        print(f'{self.__type_of_enemy} attacks for {self.attack_damage} damage')

    def special_attack(self):
        print("enemy has no special attack")

    def get_type_of_enemy(self):
        return self.__type_of_enemy
