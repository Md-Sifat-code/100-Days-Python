import random

logo=  """ 8""""8                           8""""8                    
8    " e   e eeee eeeee eeeee    8    " eeeee eeeeeee eeee 
8e     8   8 8    8   " 8   "    8e     8   8 8  8  8 8    
88  ee 8e  8 8eee 8eeee 8eeee    88  ee 8eee8 8e 8  8 8eee 
88   8 88  8 88      88    88    88   8 88  8 88 8  8 88   
88eee8 88ee8 88ee 8ee88 8ee88    88eee8 88  8 88 8  8 88ee 
                                                           
                                                                                   
"""
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
numbers = [1,6,16,24,30,39,45,50,57,61,72,77,85,91,99,100]
my_number = int(random.choice(numbers))

dificulty = input("Choose a Dificulty. Type 'easy' or 'hard' ")
chances = 0
if dificulty == "easy":
    print("You have 10 attemps remaining to guees the number")
    chances += 10
else:
    print("You have 5 attemps remaining to guees the number")
    chances +=5

while chances > 0:
    guess = int(input("Guess the number: "))
    if guess == my_number:
        print("You won")
        break
    elif guess > my_number:
        print("To High")
        chances -=1
    else:
        print("Too Low")
        chances -=1