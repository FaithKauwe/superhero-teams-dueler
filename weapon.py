import random
from ability import Ability

class Weapon(Ability):
    def attack(self):
        return random.randint(self.max_damage // 2, self.max_damage)
    def __str__(self):
        return f"Weapon: {self.name}"