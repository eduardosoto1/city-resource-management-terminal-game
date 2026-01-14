# This is a python terminal based resource management game.
# The player must take care of their money, water, food, city's rating %, population, and the number of structures they have in their city.
# The player can buy resources like wood, metal, ore, animals, money to better their city. 
# TO WIN, Get a population over 5,000 without water or food being less than zero.
# Created by: XX
# Date: 12/13/2025 - 

# How does turn based mechanism work?:
# - Player decides action (build, buy, assign)
# - Calculate Capacity
# - Use math formula to decrease or increase population
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
    "food": 300,    # Required for population
    "population": 10,   # number of people in city & win condition
    "ores": 0, # Rating based on city's rank  Should be 50
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
        "growth": 100,
    },
    # Money is the only one that difers from cost as you need ore to buy this one (which is why cost is 1)
    #"money": ["Money", 1, "Upkeeps workers, structures, and used for buying", 100],
    "money": {
        "name": "Money",
        "cost": 1,
        "description": "Upkeeps workers, structures, and used for buying (-1 Ore)",
        "growth": 1,
    },
}

# List of properties you can buy
structures = {
    "farm": {
        "name": "Farm",
        "description": "Gives extra food & water per farm you have (Assign worker here)",
        "quantity": 0
    },
    "house": {
        "name": "House",
        "description": "Gives place for worker to stay at (More placed, the more workers you can have)",
        "quantity": 0
    },
    "bank": {
        "name": "Bank",
        "description": "Assign worker here to earn +50 money per turn",
        "quantity": 0
    },
}

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

# Print actions player can do
def print_user_actions(actions):
    for act in actions:
        print(f"{act}")


# The Main Game Loop
def main_game(city, workers):
    turned_on = 0   # This is used on to allow one purhcase for each turn
    game_on = True
    while game_on:
        # Display city stats
        display_stats(city)

        # Output to player options they can use
        print_user_actions(actions)
        # Ask player to pick option
        try:
            choice = input("Pick Option by number: ").strip()
            choice = int(choice)
        except ValueError:
            print("Please enter options 1 between 5.")
        # Correlate player option with choice
        match choice:
            # Take player to shop menu
            case 1:
                turned_on = shop_menu(city, shop_inv, turned_on)
            # Assign workers to structures
            case 2:
                assign_worker(city, workers, structures)
            # Buy Land / Structures
            case 3: 
                buy_menu()
            # End Turn
            case 4:
                # If player loses
                game_on = process_turn(city)
                turned_on = 0
            # End game completly
            case 5:
                game_on = False
            # Option not in list
            case _:
                print("This option is not a choice, choices are 1-5")

def calculate_capacity(city):
    # Capacity comes from the lowest item we have, either water or food.
    capacity = min(city["water"], city["food"])
    capacity = int(capacity)

    # Warn player that they are going to negative meaning they will lose population
    if capacity < 0:
        print("WARNING: Food & water is below zero! Buy Resources before you risk losing population")
    return capacity

# Grows or decreases
def adjust_pop(capacity):
    # Initial population is 10
    init_pop = 10
    # Initial food is 100
    init_resource = 100
    # If the lowest resource is higher than the inital resource, use highest growth rate
    # Increase population by formula
    if capacity > init_resource:
        growth_rate = 0.5
        change = population_formula(init_pop, growth_rate, capacity)
        # Change population by the number given from formula
        city["population"] += change
    # Growth rate is by 0.3 and it decreases
    else:
        growth_rate = 0.3
        change = population_formula(init_pop, growth_rate, capacity)
        # Change population and decrease it by formula
        city["population"] -= change

    # Decrease resources
    city["water"] -= city["population"]
    city["food"] -= city["population"]

# Get population formula, uses logistic population growth formula
def population_formula(n, r, k):
    # Let r be the growth rate
    # Let n be the initial population
    # let k be the capacity
    new_pop = r * n * ((k - n)/k)
    new_pop = int(new_pop)
    return new_pop


# After each turn, process everything that needs to happen
def process_turn(city):
   # Get the capacity for rating
   capacity = calculate_capacity(city)
   # Adjust city rating
   adjust_pop(capacity)

   # Check if player wins or loses
   if city["population"] < 0:
       return False
   if city["population"] > 5000:
       print("You won!! Feel free to leave or continue playing.")
   else:
       return True

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
    # Get each item details based on whats in the shop
    for key, value in shop_inv.items():
        for y in value:
            # Update the key for each first letter to be capatailized
            print(f"{y}: {value[y]:<10}")
        print("-" * 20)

# Updates the shop.
def shop_menu(city, shop_inv, turn):
    # Print out each selection
    print_shop(shop_inv)
    # Enforce one purchase per turn
    # If more than 1, player should not purchase anything
    while turn == 0:
        # Ask player to pick item corresponding to name
        choice = input("Pick Option by name:\n> ").lower()
        # If the choice matches the item name, buy it
        try:
            choice = get_shop_key(shop_inv, choice)
            # Match cost and subtract it from inventory
            if shop_inv[choice]["cost"] == 1:
                # If player doesn't have ores, take them back to choosing.
                if city["ore"] < 0:
                    print("You do not have enough ore to purchase any")
                    return 
                # Remove the cost by one 
                city["ore"] -= 1
                print("You have chosen the ore")
            turn += 1
            return turn
        except KeyError:
            print("Name not found, try again.")

# Go through each name and 
def get_shop_key(shop_inv, choice):
    for key, value in shop_inv.items():
        search_key = key
        if key == choice:
            return search_key

# Buy Shop for structure or land
def buy_menu():
    # Ask user if they want to purchase structure or land
    options = ("Buy Structure", "Buy Land")
    # Used to update number list
    i = 1
    # Create empty space from status to choices to pick from
    print()
    # Print out options to pick from
    for option in options:
        print(f"{i}: {option}")
        i += 1
    choice = input("Pick option corresponding to number: ").strip()
    choice = int(choice)

    # Correspond number values with option
    match choice:
        case 1: 
            # Buy Structure
            buy_struct()
        case 2:
            # Buy Land
            buy_land()
        case _:
            # No option selected
            print("This option does not count. Try Again")
            pass
# Output the structures in a formatted way
def print_struct(structures):
    print("-" * 15)
    for i, j in structures.items():
        for y in j:
            print(f"{y}: {j[y]}")
        print("-" * 15)

# Buy Structure (Found in buy_place)
def buy_struct():
    # If no land available, do not run function
    if city["land"] <= city["structures"]:
        print(f"All your current land is filled! Buy more using option 2.")
        return
    # Output Structure name & its description
    print_struct(structures)    
    # Ask user what they would like to do
    choice = input("Pick by name")
    # Apply effect based on what structure does

# Buying land ( Selected in buy_place() )
def buy_land():
    price_per_land = 50
    # Print out the cost of each land
    print(f"Cost per land: ${price_per_land}\n")
    # Then make the player pick how much land they would like to buy (Max is 50) 
    amount = input("> How much land would you like to purchase: ")
    try:
        amount = int(amount)
        cost = price_per_land * amount
    except ValueError:
        print("Please insert number to purchase amount of land")
    # If the player does not have enough for number they picked, show how much more money they would need
    if city["money"] < cost:
        print("You do not have enough to purchase this")
        price_needed = cost - city["money"]
        print(f"Collect ${price_needed}")
        return

    # Remove money from player based on amount
    city["money"] -= cost
    # Add land based on amount
    city["land"] += amount

if __name__ == "__main__":
    main()
