# This is a python terminal based resource management game.
# The player must take care of their money, water, food, city's rating %, population, and the number of structures they have in their city.
# The player can buy resources like wood, metal, ore, animals, money to better their city. 
# TO WIN, Get a population over 5,000 without water or food being less than zero.
# Created by: XX
# Date: 12/13/2025 - 

# How does turn based mechanism work?:
# - Player decides action (build, buy, assign)
# - Calculate Capacity
# - Adjust the Rating
# - Adjust the Population based on rating
# - Consume resources based on population size
# - Check if the player win or loses

import math

WIN_POPULATION = 5000   # Amount of population needed to win
MAX_WORKERS = 5 # Max workers a player can have
RESOURCE_CONSUMPTION = 1    # How much one population takes of a resource

# Actions player can use in the game
actions = ["1. Buy / Sell Resources | Buy Workers", "2. Assign Workers", "3. Buy Land / Build Structure", "4. End turn", "5. Quit"]

# This is the city's information
city = {
    "money": 5000,  # Currency in the game
    "water": 300,   # Required for population
    "food": 100,    # Required for population
    "population": 10,   # number of people in city & win condition
    "rating": 40.0, # Rating based on city's rank  Should be 50
    "workers": 0,   # Workers are used increase ONE of your productions much faster
    "land": 1,  # Used to build structures
    "structures": 0,    # Build structures only on land you own
}

# This is used to determine how much workers take up of resource 
workers = {
    "food": 0,
    "water": 0,
    "money": 0,
}


# The shop inventory, should contain name, price. what it affects, and by how much?
shop_inv = {
    # Worker costs 2000 each, they can be assigned to collect a specific resource if structure permits, and they can collect 10 of the resource
    "worker": {
        "name": "Worker",
        "cost": 2000,
        "description": "Used to assign workers to structure",
        "growth": 10
    },
    # Wood is used to build structures
    "wood": {
        "name": "Wood",
        "cost": 300,
        "description": "Builds structures",
        "growth": 1
    },
    # Metals is used build power grids and infrastructure
    #"metals": ["Metals", 300, "Power grid & infrastructure (FOR LATER)", 1],
    "metals": {
        "name": "Metals",
        "cost": 300,
        "description": "Builds power grid & infrastructure",
        "growth": 1
    },
    # Ores will be used to sell to gain money or invest (FUTURE)
    #"ore": ["Ore", 300, "Sell for money or (INVEST | FOR FUTURE)", 1],
    "ore": {
        "name": "Ore",
        "cost": 300,
        "description": "Sell for money",
        "growth": 1
    },
    # Animals will convert into food and water for the city's population
    #"animals": ["Animals", 300, "Converts into food & gives water as well", 100],
    "animals": {
        "name": "Animals",
        "cost": 300,
        "description": "Converts into food & gives water as well",
        "growth": 100
    },
    # Money is the only one that difers from cost as you need ore to buy this one (which is why cost is 1)
    #"money": ["Money", 1, "Upkeeps workers, structures, and used for buying", 100],
    "money": {
        "name": "Money",
        "cost": 1,
        "description": "Upkeeps workers, structures, and used for buying (-1 Ore)",
        "growth": 1
    },
}

structures = {
    "farm": "Workers assigned here",
    "house": "Used to fill up population",
}

# Used to adjust the city's populating and rating
def adjust_population(city, workers, capacity, rating_bonus, growth_rate):
    try:
        pressure = city["population"] / capacity
    except ZeroDivisionError:
        pressure = city["population"] / 1
    # Adjust population based on current recourses
    if city["rating"] < 100:
        if city["population"] <= capacity:
            # Grow by small fraction of population
            city["rating"] += (1 - pressure) * rating_bonus
            fixed_num = f"{city["rating"]:.2f}"
            fixed_num = float(fixed_num)
            city["rating"] = fixed_num
        else:
            # lose population
            city["rating"] -= (pressure - 1) * rating_bonus
            fixed_num = f"{city["rating"]:.2f}"
            fixed_num = float(fixed_num)
            city["rating"] = fixed_num
    # Clamp the city ratings
    city["rating"] = max(0, min(100, city["rating"]))

    growth = 1
    rating_factor = (city["rating"] - 50) / 50
    growth += city["population"] * rating_factor * growth_rate
    growth = int(growth)
    city["population"] += growth
    growth -= growth

    city["population"] = max(0, city["population"])



def process_turn(city, worker):
    # Rating gain/loss
    RATING_BONUS = 2
    # Used to see how much population grows by
    GROWTH_RATE = 0.10

    # Calculate capacity
    capacity = min(city["water"], city["food"])
    # Do resource consumption
    RESOURCE_CONSUMPTION = city["population"]
    city["water"] -= RESOURCE_CONSUMPTION
    city["food"] -= RESOURCE_CONSUMPTION

    # Adjust population
    adjust_population(city, workers, capacity, RATING_BONUS, GROWTH_RATE)

    # Implement win / lose condition
    if city["rating"] <= 0 or city["population"] <= 0 or (city["water"] <= 0 or city["food"] <= 0):
        print("You lose")
        return False
    elif (city["rating"] >= 80.00 and city["population"] >= WIN_POPULATION) and (city["water"] > 0 and city["food"] > 0):
        print("You win")
        return False
    else:
        return True

#This assigns workers to structure
def assign_worker(city, workers, structures):
    # If player has no workers, return
    if city["workers"] < 1:
        return
    for structure in structures:
        print(structure)
def main():
    # Main Game Loop
    main_game(city, workers)

# The Main Game Loop
def main_game(city, workers):
    game_on = True
    while game_on:
        # Display city stats
        display_stats(city)

        # Output to player options they can use
        for act in actions:
            print(f"{act}")

        # Ask player to pick option
        try:
            choice = input("Pick Option by number: ").strip()
            choice = int(choice)
        except ValueError:
            print("Please enter options 1 between 5.")
        # Correlate player option with choice
        match choice:
            case 1:
                shop_menu(city, shop_inv)
            case 2:
                assign_worker(city, workers, structures)
            case 3: 
                pass
            case 4:
                game_on = process_turn(city, workers)
            case 5:
                game_on = False
            case _:
                print("This option is not a choice, choices are 1-5")

# This will change the city's rating
def adjust_rating():
    ...

# This will change the city's population
def adjust_population():
    ...

# This will display the city's information
def display_stats(city):
    # Output to player city for readibility
    print("-" * 15)
    print("--YOUR CITY--")
    print("-" * 15)
    for key, value in city.items():
        print(f"{key}: {value}")
    print()


# Prints out the shop
def print_shop(shop_inv):
    for key, value in shop_inv.items():
        name, price, description, growth = value
        print(f"Name: {name:<10} Price:${price:<10} Info:{description:<10} +{growth:<10}")

# Updates the shop.
def shop_menu(city, shop_inv):
    turn_used = 0
    # Print out each selection
    print_shop(shop_inv)
    # Enforce one purchase per turn
    # If more than 1, player should not purchase anything
    while turn_used == 0:
        choice = input("Pick Option by name:\n> ").lower()
        # If the choice matches the item name, buy it
        try:
            choice = get_shop_key(shop_inv, choice)
            if shop_inv[choice]:
                turn_used += 1
        except KeyError:
            print("Name not found, try again.")

# Go through each name and 
def get_shop_key(shop_inv, choice):
    for key, value in shop_inv.items():
        search_key = key
        if key == choice:
            return search_key

if __name__ == "__main__":
    main()
