# Define a function to calculate the required number of paint cans
def pain_calculator(height, width, coverage):
    # Calculate the number of cans required by dividing the wall area by coverage
    number_of_cans = (height * width) / coverage
    # Return the result
    return number_of_cans

# Prompt the user to input the height of the wall and convert it to a float
height_of_wall = float(input("Enter the height of the wall: "))

# Prompt the user to input the width of the wall and convert it to a float
width_of_wall = float(input("Enter the width of the wall: "))

# Call the function with the user-provided height and width, and a set coverage value of 5
print(pain_calculator(height_of_wall, width_of_wall, coverage=5))
