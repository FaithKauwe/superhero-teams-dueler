from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
    def __init__(self):
        self.team_one = Team("Team One")
        self.team_two = Team("Team Two")

    def create_ability(self):
        '''Prompt for Ability information
            return Ability with values from user Input
        '''
        name = input("What is the ability name?  ")
        max_damage = int(input("What is the max damage of the ability?  "))
        return Ability(name, max_damage)
    
    def create_weapon(self):
        '''Prompt user for Weapon information
            return Weapon with values from user input.
        '''
        name = input("What is the weapon name?  ")
        max_damage = int(input("What is the max damage of the weapon? "))
        return Weapon(name, max_damage)
    
    def create_armor(self):
        '''Prompt user for Armor information
          return Armor with values from user input.
        '''
        name = input("What is the armor name?  ")
        max_block = int(input("What is the max block of the armor?"))
        return Armor(name, max_block)
    
    def create_hero(self):
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
            add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
            if add_item == "1":
                hero.add_ability(self.create_ability())
            elif add_item == "2":
                hero.add_weapon(self.create_weapon())
            elif add_item == "3":
                hero.add_armor(self.create_armor())
        return hero
    
    def build_team_one(self):
        """
        prompt the user to build team_one
        """
        num_of_team_members = int(input("How many members would you like on Team One?\n"))
        for i in range(num_of_team_members):
            hero = self.create_hero()
            self.team_one.add_hero(hero)
        print(f"Team One: {[hero.name for hero in self.team_one.heroes]}")

    def build_team_two(self):
        """
        prompt the user to build team_two
        """
        num_of_team_members = int(input("How many members would you like on Team Two?\n"))
        for i in range(num_of_team_members):
            hero = self.create_hero()
            self.team_two.add_hero(hero)
        print(f"Team Two: {[hero.name for hero in self.team_two.heroes]}")

    def team_battle(self):
        print("For those about to rock, we salute you...")
        self.team_one.attack(self.team_two)
        print("Team battle finished.")

    def show_stats(self):
        print("\n")
        print(self.team_one.name + " statistics: ")
        self.team_one.stats()
        print("\n")
        print(self.team_two.name + " statistics: ")
        self.team_two.stats()
        print("\n")
        # This is how to calculate the average K/D for Team One
        team_kills = 0
        team_deaths = 0
        for hero in self.team_one.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(self.team_one.name + " average K/D was: " + str(team_kills/team_deaths))
        # reassign variables to 0 to use for Team2 stats
        team_kills = 0
        team_deaths = 0
        for hero in self.team_two.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(self.team_two.name + " average K/D was: " + str(team_kills/team_deaths))

        for hero in self.team_one.heroes:
            if hero.deaths == 0:
                print("survived from " + self.team_one.name + ": " + hero.name)

        for hero in self.team_two.heroes:
            if hero.deaths == 0:
                print("survived from " + self.team_two.name + ": " + hero.name)

if __name__ == "__main__":
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats()