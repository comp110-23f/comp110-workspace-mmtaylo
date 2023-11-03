"""Instantiating a class."""
# making pizzas

# where we instantiate the class we defined in classes.py (pizza.py)
# we are creating objects that belong to that^ class

from lessons.classes.pizza import Pizza

my_pizza: Pizza = Pizza("large", 10, True) # constructor

# accessing/setting attributes
# my_pizza.size = "medium"
# my_pizza.toppings = 10
# my_pizza.gluten_free = True

# # printing out the variable "my_pizza"
# print("my_pizza: ")
# # shows where it is stored
# print(my_pizza)

# # printing out the class Pizza
# print("Pizza: ")
# # shows where it is stored
print(Pizza) 

# printing out an attribute
print("Size Attribute: ")
# prints out the actual attribute!
print(my_pizza.size)

sals_pizza: Pizza = Pizza("medium", 5, False)

# calling price method
print(my_pizza.price())
print(sals_pizza.price())


my_pizza.add_toppings(2)
print(my_pizza.toppings)
print(my_pizza.price())

my_other_pizza: Pizza = my_pizza.make_new_pizza_add_toppings(2)
print(my_other_pizza.toppings)
print(my_pizza.toppings)