def turn_left():
    print("Turn left")
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def move():
    print("Moving")
front_is_clear =True
while front_is_clear:
    move()
turn_left()
at_goal = True
while not at_goal:
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear:
        move()
    else:
        turn_left()


# This project based on a project on the website where we need to help a robot to escape a maze. this code is related with that









