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