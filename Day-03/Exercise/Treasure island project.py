print("Welcome to Treasure island \n Your mission is to find the treasure!!")

x = input("You are at a Cross Road where you want to go? Right or left !")

if x == "right":
    print("Game over")
elif x == "left":
    y = input("Now you have to cross a Lake! \n Would you like to wait for a Boat or want to swim?")
    if y== "swim":
        print("Game Over")
    elif y == "wait":
        print("Your successfully came to the Island")
        z = input("There is 3 door Red / Blue / yellow . Which one you would like to choose? ")
        if z == "Red":
            print("Game Over!")
        elif z == "Blue":
            print("Game Over!")
        else:
            print("You Got The Treasure")
else:
    print("Come Back Tmr")
