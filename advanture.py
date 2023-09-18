discription = "big room"
doors = ["north", "south", "east", "west"]

# welcome screen
print("Welcome to my first game in Python")
print("__________________________________________")
print()
# mainloop
run = True
while run:
    # print room
    print("you are standing in" + " " + discription)
    print("And there are doors to your: ", doors)
    # .
    directions = ""
    for directions in doors:
        directions = directions + ". " + directions
    directions = directions[2:]
    print(directions)

    print("what do u want to do?")
    print("1. go north")
    print("2. go south")
    print("3. go east")
    print("4. go west")
    print("5. look")
    print("0. quit game")

    # ask user for input
    choice = input("please enter your choice : ")

    # santisize user input
    if not choice.isnumeric():
        print("sorry! Did not understand what u meant, Please give a number")
        continue

    choice = int(choice)
    if choice == 0:
        run = False
    elif choice == 1:
        print(
            "you are going north, take a look at the nice view of the city from the window"
        )
    elif choice == 2:
        print("you are going south")
    elif choice == 3:
        print("you are going east")
    elif choice == 4:
        print("you are going west")
    elif choice == 5:
        print("can not find anything new")
    else:
        print("you asked for something i can no t do!")
