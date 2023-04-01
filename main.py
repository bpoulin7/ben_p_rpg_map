#-----------------------------------------------------------------------------
# Created by Ben P
# Date: 31/3/2023
# version 3
#-----------------------------------------------------------------------------
"""A simple map movement game set in Ancient Mesopotamia."""
#-----------------------------------------------------------------------------
import random
import maptiles
import objects
import items


# Global Variables ###########################################################
row = 4  # east-west coordinate reference on map
col = 4  # north-south coordinate reference on map
map = [
    # simple map of 15th century BCE Mesopotamia; start location is Ur (4,4)
    ["karkemish","washukanni","nineveh","erbil","mountains"],
    ["ugarit","emar","ashur","arrapkha","mountains"],
    ["sidon","mari","kurigalzu","sippar","mountains"],
    ["tyre","desert","desert","babylon","susa"],
    ["jericho","desert","desert","uruk","ur"]
]
inventory = []
actions = ["travel", "inventory", "map", "quit"]
valid_directions = ["north", "south", "east", "west"]
dir_abb = ["n", "s", "e", "w"]


# Functions ##################################################################
def movement():
    """Allows movement around the map. Requires cardinal direction input,
    prevents movement outside map boundary, and accounts for invalid input.
    Random chance of finding objects with each movement.
    """
    global row, col
    current_location = map[row][col]
    stopped = False
    print("Directions:")
    for direction in valid_directions:
        print(f" - {direction}")
    direction_input = input("Which direction? ").lower()
    if direction_input in valid_directions or direction_input in dir_abb:
        if (direction_input == "north" or
            direction_input == "n"):
            if row == 0:
                print("You have reached the edge of the map.")
                stopped = True
            elif row > 0:
                row = row - 1
        elif direction_input == "south" or direction_input == "s":
            if row == 4:
                print("You have reached the edge of the map.")
                stopped = True
            elif row < 4:
                row = row + 1
        elif direction_input == "east" or direction_input == "e":
            if col == 4:
                print("You have reached the edge of the map.")
                stopped = True
            elif col < 4:
                col = col + 1
        elif direction_input == "west" or direction_input == "w":
            if col == 0:
                print("You have reached the edge of the map.")
                stopped = True
            elif col > 0:
                col = col - 1
    elif (direction_input.lower() == "quit" or
          direction_input.lower() == "exit"):
        # allows exiting game while in directions input
        confirm_quit = input("Are you sure you want to quit? ")
        if confirm_quit.lower() == "yes" or confirm_quit.lower() == "y":
            print("Leaving game...")
            quit()
    else:
        # accounting for invalid input
        print("Invalid direction!")
        stopped = True
    current_location = map[row][col] # update position after movement
    if stopped == False:
        # random chance of finding objects while moving
        if current_location == "desert":
            found_object = random.choices(["empty", "oasis"], [95, 5], k = 1)
            if found_object != ["empty"]:
                print(f"\nYou found a {found_object}!")
        else:
            found_object = (random.choices(["empty", "chest", "ally", 
                                            "enemy"], [50, 20, 15, 15],
                                           k = 1))
            if found_object != ["empty"]:
                print(f"\nYou found a {found_object}!")
                if found_object == ["chest"]:
                    found_item = (random.choices(["empty", "sword", "shield", 
                                                  "armor"], [25, 25, 25, 25], 
                                                 k = 1))
                    if found_item != ["empty"]:
                        print(f"There is {found_item} in the chest.")
                        inv_add = input("Add to inventory? ")
                        if inv_add.lower() == "yes" or inv_add.lower() == "y":
                            print(f"{found_item} added to inventory")
                            inventory.append(found_item)
                    else:
                        print("The chest was empty!")
                elif found_object == ["enemy"]:
                    print("Run away!")
                elif found_object == ["ally"]:
                    print("How nice. Moving on.")
    if stopped == False:
        # print new location after moving
        if current_location == "desert" or current_location == "mountains":
            print("\nThere are "
                  + maptiles.map_tiles[current_location]["desc"])
            print("It is not wise to stay here long")
        else:
            print("\nWelcome to "
                  + maptiles.map_tiles[current_location]["desc"])


def quitgame():
    """Function for leaving game that asks for confirmation."""
    confirm_quit = input("Are you sure you want to quit? ").lower()
    if confirm_quit == "yes" or confirm_quit == "y":
        print("Leaving game...")
        quit()

# Main #######################################################################
print("Welcome to the Dawn of Civilization!")
print("You are a warrior from Egypt currently in Sumer.")
print("Your goal is to get back home.")
while True:
    # prints description of current location and brings up option menu
    print("\nActions:")
    for action in actions:
        print(f" - {action}")
    input_choice = input("\nWhat would you like to do? ").lower()
    # player action options (move or exit game)
    if input_choice in actions:
        if input_choice == "travel":
            movement()
        elif input_choice == "inventory":
            print("\nInventory:")
            for item in inventory:
                print(item)
        elif input_choice == "map":
            with open("gamemap.txt") as file:
                minimap = file.read()
            print(minimap)
        elif input_choice == "quit":
            quitgame()
    elif input_choice == "exit":
        # alternative input for "quit"
        quitgame()
    elif input_choice == "go":
        # alternative input for "travel"
        movement()
    else:
        # accounting for invalid input
        print("Invalid choice!")