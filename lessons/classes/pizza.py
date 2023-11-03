"""Defining a class!"""
# deciding what the basic structure of our class will be

# class definitions are like roadmaps for objects that belong to the class
# you are defining the underlying structure every instance of this class will have

# looking into the future
from __future__ import annotations

class Pizza:
    
    # attributes
    # think of these as the variables each instance of my class will have
    # syntax: <name>: <type>
    size: str
    toppings: int
    gluten_free: bool

    def __init__(self, inp_size: str, inp_toppings: int, inp_gluten_free: bool):
        """My constructor."""
        # saying that for this Pizza instance (self), 
        #it's size attribute will be whatever the arguement is passed as 
        self.size = inp_size
        self.toppings = inp_toppings
        self.gluten_free = inp_gluten_free
        # returns a Pizza object


    def price(self) -> float:
        """Method Calculating the price of a pizza."""
        if self.size == "large":
            price: float = 6.25
        else:
            price: float = 5.00
        price += .75 + self.toppings
        if self.gluten_free:
            price += 1.00
        return price
    

    def add_toppings(self, num_toppings: int):
        """Function to update an attribute/add toppings to existing pizza."""
        self.toppings += num_toppings


    def make_new_pizza_add_toppings(self, num_toppings: int) -> Pizza:
        """Make a new pizza with existing pizza's propertieis and add toppings."""
        new_pizza: Pizza = Pizza(self.size, self.toppings, self.gluten_free)
        return new_pizza