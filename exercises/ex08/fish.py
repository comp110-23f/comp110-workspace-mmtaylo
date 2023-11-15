"""File to define Fish class."""


class Fish:
    """Class to create a Fish."""
    age: int
    
    def __init__(self):
        """Function to initialize a Fish's age."""
        self.age = 0
        return None
    
    def one_day(self):
        """Function to simulate one day in a Fish's life."""
        self.age += 1
        return None