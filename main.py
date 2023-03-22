#-----------------------------------------------------------------------------
# Created by Ben P
# Date: 22/3/2023
# version 002
#-----------------------------------------------------------------------------
"""A simple map movement game set in Ancient Mesopotamia."""
#-----------------------------------------------------------------------------
import random


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
map_tiles = {
    "desert" : {
        "desc" : "endless sand dunes and no civilization for miles",
        "owner" : "---"
    },
    "mountains" : {
        "desc" : "vast mountains stretching as far as the eye can see",
        "owner" : "---"
    },
    "karkemish" : {
        "desc" : "Karkemish, a legendary city on the Euphrates River",
        "owner" : "MIT"
    },
    "washukanni" : {
        "desc" : "Washukanni, the great capital of the Mittani Empire",
        "owner" : "MIT"
    },
    "nineveh" : {
        "desc" : "Nineveh, an ancient Akkadian city on the Tigris River",
        "owner" : "MIT"
    },
    "erbil" : {
        "desc" : "Erbil, a town on the edge of the civilized world",
        "owner" : "MIT"
    },
    "ugarit" : {
        "desc" : "Ugarit, a trading hub city on the Mediterranean coast",
        "owner" : "EGY"
    },
    "emar" : {
        "desc" : "Emar, a small but important trade hub on the Euphrates",
        "owner" : "MIT"
    },
    "ashur" : {
        "desc" : "Ashur, the capital of Assyria, now under Mittani control",
        "owner" : "MIT"
    },
    "arrapkha" : {
        "desc" : "Arrapkha, a secluded city on the edge of civilization",
        "owner" : "MIT"
    },
    "sidon" : {
        "desc" : "Sidon, an ancient fishing town under Egyptian control",
        "owner" : "EGY"
    },
    "mari" : {
        "desc" : "Mari, once a thriving city, now mostly abandoned",
        "owner" : "SUH"
    },
    "kurigalzu" : {
        "desc" : "Dur-Kurigalzu, the capital of Kassite Babylonia",
        "owner" : "BAB"
    },
    "sippar" : {
        "desc" : "Sippar, one of the many riverine cities of Babylonia",
        "owner" : "BAB"
    },
    "tyre" : {
        "desc" : "Tyre, one of the oldest cities on the Mediterranean",
        "owner" : "EGY"
    },
    "babylon" : {
        "desc" : "Babylon, the heart of Babylonia and Mesopotamia",
        "owner" : "BAB"
    },
    "susa" : {
        "desc" : "Susa, a major city of the Elamite Empire",
        "owner" : "ELA"
    },
    "jericho" : {
        "desc" : "Jericho, perhaps the oldest city in the world",
        "owner" : "EGY"
    },
    "uruk" : {
        "desc" : "Uruk, an old Sumerian city central to Mesopotamia",
        "owner" : "SUM"
    },
    "ur" : {
        "desc" : "Ur, a Sumerian city on the high Persian Gulf coast",
        "owner" : "SUM"
    }
}
objects = {
    # things to potentially find at different map locations
    "empty" : {
        "desc" : "nothing here"
    },
    "chest" : {
        "desc" : "a treasure chest full of valuables"
    },
    "enemy" : {
        "desc" : "some armed and hostile warriors"
    },
    "ally" : {
        "desc" : "some friendly locals who provide supplies"
    },
    "oasis" : {
        "desc" : "an oasis in the middle of the desert"
    }
}
items = {
    # things to put in inventory
    "sword" : {
        "desc" : "a blade for combat"
    },
    "shield" : {
        "desc" : "a shield for defense"
    },
    "armor" : {
        "desc" : "some armor for protection"
    }
}
inventory = []
actions = ["travel", "inventory", "quit"]
valid_directions = ["north", "n", "south", "s", "east", "e", "west", "w"]

# Functions ##################################################################


def movement():
    """Allows movement around the map. Requires cardinal direction input,
    prevents movement outside map boundary, and accounts for invalid input.
    Random chance of finding objects with each movement.
    """
    global row, col
    current_location = map[row][col]
    stopped = False
    direction_input = input("Which direction (north, south, east, or west?) ")
    if direction_input in valid_directions:
        if (direction_input.lower() == "north" or
            direction_input.lower() == "n"):
            if row == 0:
                print("You have reached the edge of the map.")
                stopped = True
            elif row > 0:
                row = row - 1
        elif (direction_input.lower() == "south" or
              direction_input.lower() == "s"):
            if row == 4:
                print("You have reached the edge of the map.")
                stopped = True
            elif row < 4:
                row = row + 1
        elif (direction_input.lower() == "east" or
              direction_input.lower() == "e"):
            if col == 4:
                print("You have reached the edge of the map.")
                stopped = True
            elif col < 4:
                col = col + 1
        elif (direction_input.lower() == "west" or
              direction_input.lower() == "w"):
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
            found_object = random.choices(["empty", "oasis"], [95, 5], k=1)
            print(f"You found a {found_object}!")
        else:
            found_object = (random.choices(["empty", "chest", "ally", 
                                            "enemy"], [50, 20, 15, 15], k=1))
            print(f"You found a {found_object}!")
            if found_object == ["chest"]:
                found_item = (random.choices(["empty", "sword", "shield",
                                              "armor"], [25, 25, 25, 25],k=1))
                if found_item != ["empty"]:
                    print(f"{found_item} added to inventory")
                    inventory.append(found_item)
                else:
                    print("The chest was empty!")
    if stopped == False:
        # print new location after moving
        if current_location == "desert" or current_location == "mountains":
            print("There are " + map_tiles[current_location]["desc"])
            print("It is not wise to stay here long")
        else:
            print("Welcome to " + map_tiles[current_location]["desc"])


# Main #######################################################################

while True:
  # prints description of current location and brings up option menu
  print("Actions:")
  for action in actions:
      print(f" - {action}")
  input_choice = input("What would you like to do? ")
  # player action options (move or exit game)
  if input_choice.lower() in actions:
      if input_choice.lower() == "travel":
          movement()
      elif input_choice.lower() == "inventory":
          print("Inventory:")
          for item in inventory:
              print(item)
      elif input_choice.lower() == "quit":
          confirm_quit = input("Are you sure you want to quit? ")
          if confirm_quit.lower() == "yes" or confirm_quit.lower() == "y":
              print("Leaving game...")
              quit()
  elif input_choice.lower() == "exit":
      # alternative input for "quit"
      confirm_quit = input("Are you sure you want to quit? ")
      if confirm_quit.lower() == "yes" or confirm_quit.lower() == "y":
          print("Leaving game...")
          quit()
  elif input_choice.lower() == "go":
      # alternative input for "travel"
      movement()
  else:
      # accounting for invalid input
      print("Invalid choice!")