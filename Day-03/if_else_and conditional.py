# Conditional statements help make decisions in code based on certain conditions.
# The 'if' statement checks if a condition is true.
# The 'else' statement runs if the 'if' condition is false.
print("Welcome to the event!")
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to enter.")
elif age >= 13:
    print("You can enter with parental supervision.")
else:
    print("Sorry, you must be at least 13 to enter.")