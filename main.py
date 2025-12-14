# This is a python terminal based resource management game.
# The player must take care of their money, water, food, city's rating %, population, and the number of structures they have in their city.
# The player can buy resources like wood, metal, ore, animals, money to better their city. 
# TO WIN, Get a population over 5,000 without water or food being less than zero.
# Created by: XX
# Date: 12/13/2025 - 

# This is the city's information
city = {
    "Money": 5000,  # Currency in the game
    "Water": 100,   # Required for population
    "Food": 100,    # Required for population
    "Population": 10,   # number of people in city & win condition
    "Rating": 50.0, # Multiplier for population growth
    "Workers": 0,   # Workers are used increase ONE of your productions much faster
    "Land": 1,  # Used to build structures
    "Structures": 0,    # Build structures only on land you own
}

# This is used to determine how much workers take up of resource 
workers = {
    "Food": 0,
    "Water": 0,
    "Money": 0,
}

# This will display the city's information
def display_stats():
    print("--YOUR CITY--")
    for key, value in city.items():
        print(f"{key}: {value}")

display_stats()

