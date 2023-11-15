"""File to define River class."""

__author__ = "730578652"

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """Class to create a River."""
    day: int  # tells you what day of the river's lifecycle you are modeling
    bears: list[Bear]  # a list of bears that stores the river's bear population
    fish: list[Fish]  # a list of fish that stores the river's fish population
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Function to check the ages of Fish and Bears; removes them from the River if they are too old."""
        fish_age_check: list[Fish] = self.fish
        bear_age_check: list[Bear] = self.bears

        for fishie in self.fish:
            if fishie.age > 3:
                fish_age_check.pop(0)

        self.fish = fish_age_check

        for teddy in self.bears:
            if teddy.age > 5:
                bear_age_check.pop(0)
        
        self.bears = bear_age_check

        return None

    def remove_fish(self, amount: int):
        """Function to remove Fish that the Bears eat."""
        for fishie in range(0, amount):
            self.fish.pop(0)
        return None

    def bears_eating(self): 
        """Function to simulate Bears eating if there are at least 5 fish in the River per Bear."""
        for teddy in self.bears:
            if len(self.fish) >= 5:
                teddy.eat(3)
                self.remove_fish(3)
        return None
    
    def check_hunger(self):
        """Function to check if a Bear's hunger score is too low; if it is, the Bear is removed."""
        bear_hunger_check: list[Bear] = self.bears

        for teddy in self.bears:
            if teddy.hunger_score < 0:
                bear_hunger_check.pop(0)

        self.bears = bear_hunger_check

        return None
        
    def repopulate_fish(self):
        """Function to add 4 new Fish to the River for every 2 existing Fish."""
        baby_fish: int = len(self.fish) // 2 * 4
        
        for fishie in range(0, baby_fish):
            self.fish.append(Fish)
        return None
    
    def repopulate_bears(self):
        """Function to add 1 new Bear to the River for every 2 Bears."""
        baby_bear: int = len(self.bears) // 2
        
        for teddy in range(0, baby_bear):
            self.bears.append(Bear)
        return None
    
    def view_river(self):
        """Function that prints out the day and it's fish and bear populations."""
        fish_poulation: int = len(self.fish)
        bears_population: int = len(self.bears)
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish Population: {fish_poulation}")
        print(f"Bear population: {bears_population}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Function to call one_river_day 7 times (for one week)."""
        i: int = 0
        while i < 7:
            self.one_river_day()
            self.day += 1
        return None