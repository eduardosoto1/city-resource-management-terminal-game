# This is a python terminal based resource management game.
# The player must take care of their money, water, food, city's rating %, population, and the number of structures they have in their city.
# The player can buy resources like wood, metal, ore, animals, money to better their city. 
# TO WIN, Get a population over 5,000 without water or food being less than zero.
# Created by: XX
# Date: 12/13/2025 - 

WIN_POPULATION = 5000   # Amount of population needed to win
MAX_WORKERS = 5 # Max workers a player can have
RESOURCE_CONSUMPTION = 10    # How much one population takes of a resource
GAME_ON = True

# Actions player can use in the game
actions = ["1. Buy / Sell Resources | Buy Workers", "2. Assign Workers", "3. Buy Land / Build Structure", "4. End turn", "5. Quit"]

# This is the city's information
city = {
    "money": 5000,  # Currency in the game
    "water": 100,   # Required for population
    "food": 100,    # Required for population
    "population": 10,   # number of people in city & win condition
    "rating": 50.0, # Multiplier for population growth
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


def process_turn(city, workers, game_status):
    # Do resource consumption
    city["water"] -= RESOURCE_CONSUMPTION
    city["food"] -= RESOURCE_CONSUMPTION
    # Implement win / lose condition
    if city["rating"] < 25.0 and city["population"] < 0 or city["water"] < 0 or city["food"] < 0:
        print("You lose")
        game_status = False
    elif city["rating"] > 0 and city["population"] == WIN_POPULATION and city["water"] > 0 and city["food"] > 0:
        print("You win")
    else:
        pass


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
        choice = input("Pick Option (By Number): ").strip()
        choice = int(choice)
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
                process_turn(city, workers, game_on)
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
