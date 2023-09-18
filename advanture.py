# Welcoming Screen (Function).
def WlcScreen():
    print(
        "Welcome to my first game in Python. Its a simple game that allows you to choose one of som options to make a movement "
    )
    print("__________________________________________")
    print()


# Description and the view of the room (Function) .
def displayRoom(discription, doors):
    print("you are standing in" + " " + discription)
    print("And there are doors to your: ", doors)
    # Movements that are available in the room.
    directions = ""
    for directions in doors:
        directions = directions + ". " + directions
    directions = directions[2:]
    print(directions)
    print()


# Option menu for the player (Function).
def optionMenu():
    print("what do u want to do?")
    print("1. go north")
    print("2. go south")
    print("3. go east")
    print("4. go west")
    print("5. look")
    print("0. quit game")


discription = "big scary room "
doors = ["north", "south", "east", "west"]

###############################################
###############################################
# Main Program

# Welcoming Screen
WlcScreen()

# mainloop
run = True
while run:
    # print the room for the player
    displayRoom(discription, doors)

    # showing the menu input for the player
    optionMenu()

    # ask player for input
    choice = input("please enter your choice : ")

    # santisize user input
    if not choice.isnumeric():
        print("sorry! Did not understand what u meant, Please give a number")
        continue
    # Check player choises
    choice = int(choice)
    if choice == 0:
        run = False
    elif choice == 1:
        print(
            "You are going north, Good choice. That is the door that promises freedom ,take a deep breath and push the door open and step inside."
        )
    elif choice == 2:
        print("you are going south ")
    elif choice == 3:
        print(
            "This door is locked, you need to get more damage points to be able to open this door"
        )
    elif choice == 4:
        print("Sorry, you reach a dead end, surrounded by walls closing in. Wasted")
    elif choice == 5:
        print("can not find anything new")
    else:
        print("you asked for something i can not do!")
