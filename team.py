import random
from hero import Hero

class Team:
  def __init__(self, name):
    ''' Initialize your team with its team name and an empty list of heroes
    '''
    self.name = name
    self.heroes = list()

  def add_hero(self, hero):
        self.heroes.append(hero)

  def remove_hero(self, name):
    '''Remove hero from heroes list.
    If Hero isn't found return 0.
    '''
    foundHero = False
    # loop through each hero in our list
    for hero in self.heroes:
        # if we find them, remove them from the list
        if hero.name == name:
            self.heroes.remove(hero)
        # set our indicator to True
            foundHero = True
  # if we looped through our list and did not find our hero,
  # the indicator would have never changed, so return 0
    if not foundHero:
        return 0
  
  def view_all_heroes(self):
        if len(self.heroes) > 0:
            for hero in self.heroes:
                print(hero.name)
        else:
            return "No heroes Found"

# Print team statistics     
  def stats(self):
        for hero in self.heroes:
            if hero.deaths > 0:
                kd = hero.kills / hero.deaths
            else:
                kd = "{hero.name} has 0 deaths and {hero.kills} kills"
            print(f"{hero.name} Kill/Deaths:{kd}")

  def revive_heroes(self, health=100):
        ''' Reset all heroes health to starting_health'''
        for hero in self.heroes:
            hero.current_health = hero.starting_health

  def attack(self, other_team):
        living_heroes = []
        living_opponents = []

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents) > 0:
            fighting_hero = random.choice(living_heroes)
            fighting_opponent = random.choice(living_opponents)

            fighting_hero.fight(fighting_opponent)

            if fighting_hero.current_health < 0:
                living_heroes.remove(fighting_hero)

            elif fighting_opponent.current_health < 0:
                living_opponents.remove(fighting_opponent)
            
            else:
                pass

        self.stats()
        other_team.stats()

        if len(living_heroes) >= 0:
            print(f"{self.name} won!!")

        elif len(living_opponents) >= 0:
            print(f"{other_team.name} won!!")