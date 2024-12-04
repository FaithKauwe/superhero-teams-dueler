import random

class Ability:
    def __init__(self, name: str, max_damage: int):
        self.name = name
        self.max_damage = max_damage
    
    def attack(self):
        random_value = random.randint(0,self.max_damage)
        return random_value
    
    def __str__(self):
        return self.name
    

if __name__ == "__main__":
    test_ability = Ability("fireball", 39)
    print(test_ability.name)
    print(test_ability.attack())