from random import choice

set_of_choice = ['rock','paper','siger']
x = input("Enter anything from rock/paper/siger")
y = choice(set_of_choice)
if x != y:
    print("You win")
else:
    print(f"Sorry you lose. Computer choose: {y}")