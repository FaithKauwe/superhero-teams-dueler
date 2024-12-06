import random

class Armor:
    def __init__(self, name: str, max_block: int):
        self.name = name
        self.max_block = max_block

    def defend(self):
        random_value = random.randint(0,self.max_block)
        return random_value
    
if __name__ == "__main__":
  # If you run this file from the terminal
  # this block is executed.
  armor = Armor("Ice Shield", 10)
  print(armor.name)
  print(armor.defend())