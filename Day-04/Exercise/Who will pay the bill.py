from random import choice

x = input("Enter the names of your friends\n")
y = x.split(" ")
z = choice(y)
print(f"The Bill will be paid by {z}!!")