"""File to define Bear class."""


class Bear:
    """Class to create a Bear."""
    age: int
    hunger_score: int
    
    def __init__(self):
        """Function to initialize a Bear's age and hunger_score."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """Function to simulate one day in a Bears life."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Function to update a Bear's hunger score by the number of fish that it eats."""
        self.hunger_score += num_fish
        return None