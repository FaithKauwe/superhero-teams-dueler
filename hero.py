import random
from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:
  # We want our hero to have a default "starting_health",
  # so we can set that in the function header.
  def __init__(self, name, starting_health=100):

    # we know the name of our hero, so we assign it here
    self.name = name
    # similarly, our starting health is passed in, just like name
    self.starting_health = starting_health
    # when a hero is created, their current health is
    # always the same as their starting health (no damage taken yet!)
    self.current_health = starting_health
    # abilities and armors don't have starting values,
    # and are set to empty lists on initialization
    self.abilities = list()
    self.armors = list()
    self.kills: int = 0
    self.deaths: int = 0

  def add_kill(self):
        self.kills += 1

  def add_death(self):
        self.deaths += 1
  
  def fight(self, opponent):
    winner = random.choice([self, opponent])
    return f"{winner.name} wins!"
  
  def add_ability(self, ability):
    self.abilities.append(ability)
  
  def attack (self):
    total_damage = 0
    for ability in self.abilities:
      total_damage += ability.attack()
    return total_damage  
  
  def add_armor(self, armor):
    self.armors.append(armor)

  def add_weapon(self, weapon):
     self.abilities.append(weapon)
  
  def defend(self):
    total_defense = 0
    for armor in self.armors:
      total_defense += armor.defend()
    return total_defense
  
  def take_damage(self, damage):
    damage_taken = damage - self.defend() 
    self.current_health -= damage_taken
    return self.current_health
  
  def is_alive(self):
        """
        return True or False depending on whether the hero is alive or not
        """
        if self.current_health <= 0:
            print(f"{self.name} has fainted!")
            return False
        else:
            print(f"{self.name} is still up!")
            return True
  def fight(self, opponent):
        """
        current hero will take turns fighting the opponent hero passed in
        """
        while self.is_alive() == True and opponent.is_alive() == True:
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())
            print(f"{self.name} has {self.current_health} hp and {opponent.name} has {opponent.current_health} hp")

        if opponent.is_alive() == False:
            self.add_kill()
            opponent.add_death()
            print(f"{self.name} won!")

        if self.is_alive() == False:
            opponent.add_kill()
            self.add_death()
            print(f"{opponent.name} won!")

# this line should exist in any python file in a multi file project. otherwise, every file will run
# everytime any file is run.  I want to control when and how scripts/ files run, this line allows that

if __name__ == "__main__":
  # If you run this file from the terminal
  # this defend is executed.
  wonder_woman = Hero("Diana", 300)
  batman = Hero("Bruce", 189)
  print(f"WonderWoman Starting Health: {wonder_woman.current_health}")
  flying = Ability("flying", 300)
  fireball = Ability("fireball", 389)
  lightning = Ability("lightning", 313)
  ice_shield = Armor("ice shield", 269)
  force_field = Armor("force field", 419)
  lasso = Weapon("Lasso of Truth", 96)
  wonder_woman.add_ability(flying)
  wonder_woman.add_ability(lightning)
  wonder_woman.add_armor(ice_shield)
  wonder_woman.add_armor(force_field)
  wonder_woman.take_damage(60)
  batman.add_armor(force_field)
  print(f"Name: {wonder_woman.name}")
  print(f"Wonder Woman Abilities: {[ability.name for ability in wonder_woman.abilities]}")
  print(f"Wonder Woman Attack: {wonder_woman.attack()}")
  print(f"Wonder Woman Armor: {[armor.name for armor in wonder_woman.armors]}")
  print(f"Wonder Woman Defense: {wonder_woman.defend()}")
  print(f"WonderWoman Current Health: {wonder_woman.current_health}")
  wonder_woman.is_alive()
  