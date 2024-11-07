def turnLeft():
    print("turn left")

def turnRight():
    print("turn left")
    print("turn left")
    print("turn left")

def looping():
    print("move")
    turnLeft()
    print("move")
    turnRight()
    print("move")
    turnRight()
    print("move")
    turnLeft()

flag = False
number = 6

while not flag:
    if number == 1:
        flag = True
    else:
        looping()
    number -= 1

# this i an exercise how we can impliment while loop