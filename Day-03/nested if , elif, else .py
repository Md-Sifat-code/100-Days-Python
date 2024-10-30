# Nested 'if' statements allow for additional decision-making within an existing condition.
# After an initial 'if' condition, we can add further checks.

print("Welcome to the amusement park!")
height = int(input("Enter your height in cm: "))
age = int(input("Enter your age: "))

if height >= 140:
    if age >= 18:
        print("You can enter all rides, including the thrill rides!")
    elif age >= 12:
        print("You can enter, but some thrill rides may be restricted.")
    else:
        print("You can enter the park, but only with adult supervision.")
else:
    print("Sorry, you need to be taller to enter the amusement park.")
