# global variables

row = 4
col = 4

map = [
    ["Karkemish","Washukanni","Nineveh","Erbil","mountains"],
    ["Ugarit","Emar","Ashur","Arrapkha","mountains"],
    ["Sidon","Mari","Dur-Kurigalzu","Sippar","mountains"],
    ["Tyre","desert","desert","Babylon","Susa"],
    ["Jericho","desert","desert","Uruk","Ur"]
]

#sub-menu (which direction)

valid_directions = ["north", "n", "south", "s", "east", "e", "west", "w"]

def movement():
    global row, col
    direction_input = input("Which direction? ")
    if direction_input in valid_directions:
        if direction_input.lower() == "north" or direction_input.lower() == "n":
            if row == 0:
                print("You have reached the edge of civilization.")
            elif row > 0:
                row = row - 1
        elif direction_input.lower() == "south" or direction_input.lower() == "s":
            if row == 4:
                print("You have reached the edge of civilization.")
            elif row <4:
                row = row + 1
        elif direction_input.lower() == "east" or direction_input.lower() == "e":
            if col == 4:
                print("You have reached the edge of civilization.")
            elif col < 4:
                col = col + 1
        elif direction_input.lower() == "west" or direction_input.lower() == "w":
            if col == 0:
                print("You have reached the edge of civilization.")
            elif col > 0:
                col = col - 1
    else:
        print("Invalid direction!")

# main

while True:
  current_location = map[row][col]
  if current_location == "desert":
      print("There are only sand dunes around, and no civilization for miles.")
      print("It is not wise to stay here long.")
  elif current_location == "mountains":
    print("Vast mountains stretch as far as the eye can see.")
    print("It is not wise to stay here long.")
  elif current_location == "Karkemish":
    print("Welcome to Karkemish, a legendary and enigmatic city on the Euphrates River.")
  elif current_location == "Washukanni":
    print("Welcome to Washukanni, the great capital of the Mittani Empire.")
  elif current_location == "Nineveh":
    print("Welcome to Nineveh, an ancient Akkadian city on the Tigris River.")
  elif current_location == "Erbil":
    print("Welcome to Erbil, a town on the edge of the civilized world.")
  elif current_location == "Ugarit":
    print("Welcome to Ugarit, a prominent trading hub city on the Mediterranean coast.")
  elif current_location == "Emar":
    print("Welcome to Emar, a small but important trade hub on the Euphrates River.")
  elif current_location == "Ashur":
    print("Welcome to Ashur, the capital of Assyria, now under control of the Mittani.")
  elif current_location == "Arrapkha":
    print("Welcome to Arrapkha, a secluded city on the eastern edge of the known world.")
  elif current_location == "Sidon":
    print("Welcome to Sidon, an ancient fishing town under Egyptian influence.")
  elif current_location == "Mari":
    print("Welcome to Mari, once the center of an empire, now largely abandoned.")
  elif current_location == "Dur-Kurigalzu":
    print("Welcome to Dur-Kurigalzu, the capital of Kassite Babylonia.")
  elif current_location == "Sippar":
    print("Welcome to Sippar, one of the many riverine cities of Babylonia.")
  elif current_location == "Tyre":
    print("Welcome to Tyre, one of the oldest cities on the Mediterranean coast.")
  elif current_location == "Babylon":
    print("Welcome to Babylon, the largest city in the world and heart of Babylonia.")
  elif current_location == "Susa":
    print("Welcome to Susa, a major city of the Elamite Empire.")
  elif current_location == "Jericho":
    print("Welcome to Jericho, perhaps the oldest city in the world.")
  elif current_location == "Uruk":
    print("Welcome to Uruk, an old Sumerian city in the middle of Mesopotamia.")
  elif current_location == "Ur":
    print("Welcome to Ur, a Sumerian city on the raised Persian Gulf coast.")
  
  print("There are no options yet, so walk!")
  movement()