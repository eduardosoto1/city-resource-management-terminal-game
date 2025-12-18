# This is a python terminal based resource management game.
# The player must take care of their money, water, food, city's rating %, population, and the number of structures they have in their city.
# The player can buy resources like wood, metal, ore, animals, money to better their city. 
# TO WIN, Get a population over 5,000 without water or food being less than zero.
# Created by: XX
# Date: 12/13/2025 - 

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
    RATING_BONUS = 3
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


# This will display the city's information
def display_stats(city):
    # Output to player city for readibility
    print("-" * 15)
    print("--YOUR CITY--")
    print("-" * 15)
    for key, value in city.items():
        print(f"{key}: {value}")
    print()

def main_game(city, workers):
    # Game Loop ends when false
    game_on = True
    while game_on:
        # Display city stats
        display_stats(city)

        # Output to player options they can do
        for action in actions:
            print(f"{action}")

        # Ask Player to pick option
        try:
            choice = input("Pick Option (By Number): ").strip()
            choice = int(choice)
        except ValueError:
            print("Please enter option by number.")
        # Correlate player choice with action
        match choice:
            # Buy / Sell Resources | Buy Workers
            case 1:
                print("Option 1")
                pass
            case 2:
                print("Option 2")
                pass
            case 3:
                print("Option 3")
                pass
            case 4:
                game_on = process_turn(city, workers)
                pass
            case 5:
                game_on = False
            case _:
                print("This option is not a choice. Please enter number 1-5.")

def main():
    # Main Game Loop
    main_game(city, workers)

if __name__ == "__main__":
    main()
