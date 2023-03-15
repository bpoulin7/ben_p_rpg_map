#-----------------------------------------------------------------------------
# Created by Ben P
# Date: 14/3/2023
# version 001
#-----------------------------------------------------------------------------
"""A simple map movement game set in Ancient Mesopotamia."""
#-----------------------------------------------------------------------------

# Global Variables ###########################################################

row = 4  # east-west coordinate reference on map
col = 4  # north-south coordinate reference on map
# simplified map of 15th century BCE Mesopotamia
# starting location is Ur (4,4)
map = [
    ["Karkemish","Washukanni","Nineveh","Erbil","mountains"],
    ["Ugarit","Emar","Ashur","Arrapkha","mountains"],
    ["Sidon","Mari","Dur-Kurigalzu","Sippar","mountains"],
    ["Tyre","desert","desert","Babylon","Susa"],
    ["Jericho","desert","desert","Uruk","Ur"]
]
valid_directions = ["north", "n", "south", "s", "east", "e", "west", "w"]

# Functions ##################################################################


def movement():
    """Allows movement around the map. Requires cardinal direction input,
    prevents movement outside map boundary, and accounts for invalid input.
    """
    global row, col
    direction_input = input("Which direction? ")
    if direction_input in valid_directions:
        if (direction_input.lower() == "north" or
            direction_input.lower() == "n"):
            if row == 0:
                print("You have reached the edge of civilization.")
            elif row > 0:
                row = row - 1
        elif (direction_input.lower() == "south" or
              direction_input.lower() == "s"):
            if row == 4:
                print("You have reached the edge of civilization.")
            elif row <4:
                row = row + 1
        elif (direction_input.lower() == "east" or
              direction_input.lower() == "e"):
            if col == 4:
                print("You have reached the edge of civilization.")
            elif col < 4:
                col = col + 1
        elif (direction_input.lower() == "west" or
              direction_input.lower() == "w"):
            if col == 0:
                print("You have reached the edge of civilization.")
            elif col > 0:
                col = col - 1
    # accounting for invalid input
    else:
        print("Invalid direction!")


# Main #######################################################################

while True:
  # prints description of current location and brings up option menu
  current_location = map[row][col]
  if current_location == "desert":
      print("There are only sand dunes around, and no civilization for miles")
      print("It is not wise to stay here long.")
  elif current_location == "mountains":
    print("Vast mountains stretch as far as the eye can see.")
    print("It is not wise to stay here long.")
  elif current_location == "Karkemish":
    print("Welcome to Karkemish, a legendary city on the Euphrates River.")
  elif current_location == "Washukanni":
    print("Welcome to Washukanni, the great capital of the Mittani Empire.")
  elif current_location == "Nineveh":
    print("Welcome to Nineveh, an ancient Akkadian city on the Tigris River.")
  elif current_location == "Erbil":
    print("Welcome to Erbil, a town on the edge of the civilized world.")
  elif current_location == "Ugarit":
    print("Welcome to Ugarit, a trading hub city on the Mediterranean coast.")
  elif current_location == "Emar":
    print("Welcome to Emar, a small important trade hub on the Euphrates.")
  elif current_location == "Ashur":
    print("Welcome to Ashur, capital of Assyria, now under Mittani control.")
  elif current_location == "Arrapkha":
    print("Welcome to Arrapkha, a secluded city on the edge of civilization.")
  elif current_location == "Sidon":
    print("Welcome to Sidon, an ancient fishing town under Egyptian control.")
  elif current_location == "Mari":
    print("Welcome to Mari, once a thriving city, now mostly abandoned.")
  elif current_location == "Dur-Kurigalzu":
    print("Welcome to Dur-Kurigalzu, the capital of Kassite Babylonia.")
  elif current_location == "Sippar":
    print("Welcome to Sippar, one of the many riverine cities of Babylonia.")
  elif current_location == "Tyre":
    print("Welcome to Tyre, one of the oldest cities on the Mediterranean.")
  elif current_location == "Babylon":
    print("Welcome to Babylon, the heart of Babylonia and Mesopotamia.")
  elif current_location == "Susa":
    print("Welcome to Susa, a major city of the Elamite Empire.")
  elif current_location == "Jericho":
    print("Welcome to Jericho, perhaps the oldest city in the world.")
  elif current_location == "Uruk":
    print("Welcome to Uruk, an old Sumerian city central to Mesopotamia.")
  elif current_location == "Ur":
    print("Welcome to Ur, a Sumerian city on the high Persian Gulf coast.")
  # player action options (move or exit game)
  input_choice = input("What would you like to do? ")
  if (input_choice.lower() == "walk" or input_choice.lower() == "move" or
      input_choice.lower() == "go"):
      movement()
  elif input_choice.lower() == "quit" or input_choice == "exit":
      confirm_quit = input("Are you sure you want to quit? ")
      if confirm_quit.lower() == "yes" or confirm_quit.lower() == "y":
          print("Leaving game...")
          quit()
  # accounting for invalid input
  else:
      print("Invalid choice!")