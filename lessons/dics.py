"""CL07 Dictionaries Practice."""

# constructing a dictionary
ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
print("Made my dictionary!")
print(ice_cream)

# adding a key, value pair to a dictionary
ice_cream["mint"] = 3
print("After adding mint: ")
print(ice_cream)

# removing a key, value pair from a dictionary
ice_cream.pop("mint")
print("After removing mint: ")
print(ice_cream)

# accessing a value from a dictionary
print(f"There are {ice_cream['chocolate']} orders of chocolate.")

# modifying a value in a key, value pair in a dictionary
ice_cream['vanilla'] = 10
print("After changing the amount of vanilla: ")
print(ice_cream)

# printing the length of a dictionary, aka the amount of key, value pairs in a dictionary
print(f"The number of flavors we are offering is {len(ice_cream)}.")

# checking if a value is in a dictionary
print("Is chocolate in ice_cream?")
print("chocolate" in ice_cream)

# using it in a conditional
if "mint" in ice_cream:
    print(f"There are {ice_cream['mint']} orders of mint.")
else:
    print("There are no orders of mint.")

# loop through and print out every flavor and its number of orders
for key in ice_cream:
    print(f"{key} has {ice_cream[key]} orders.")
