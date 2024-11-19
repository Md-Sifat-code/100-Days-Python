from art import ascii_art  # Make sure 'ascii_art' is imported correctly

# Display the ASCII art
print(ascii_art)

# Initialize the onemore variable
onemore = "y"

# Start the calculator loop
while onemore == "y":
    # Input the first number
    x = int(input("What is the first number? \n"))

    # Input the operator
    y = input("+\n-\n*\n/\nPick an Operation:\n")

    # Input the second number
    z = int(input("What is the next number: "))

    # Perform the operation based on the operator
    if y == "+":
        result = x + z
        print(f"{x} {y} {z} = {result}")
    elif y == "-":
        result = x - z
        print(f"{x} {y} {z} = {result}")
    elif y == "*":
        result = x * z
        print(f"{x} {y} {z} = {result}")
    elif y == "/":
        if z != 0:  # Check to avoid division by zero
            result = x / z
            print(f"{x} {y} {z} = {result}")
        else:
            print("Division by zero is not allowed. Please try again.")
    else:
        print("Invalid operator. Please enter a valid operation.")

    # Ask if the user wants to continue calculating
    onemore = input("Type 'y' to continue calculating or any other key to exit: ").lower()

print("Thank you for using the calculator!")
