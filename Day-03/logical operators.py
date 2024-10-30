# Function to calculate BMI
def calculate_bmi(weight, height):
    return weight / (height ** 2)

# Main program
try:
    # Input weight in kilograms and height in meters
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (m): "))

    # Calculate BMI
    bmi = calculate_bmi(weight, height)

    # Display the BMI
    print(f"Your BMI is: {bmi:.2f}")

    # Categorize BMI using logical operators
    if bmi < 18.5:
        print("You are underweight.")
    elif (bmi >= 18.5 and bmi < 25):
        print("You have a normal weight.")
    elif (bmi >= 25 and bmi < 30):
        print("You are overweight.")
    elif (bmi >= 30 or bmi >= 40):  # Added condition to illustrate usage of 'or'
        print("You are obese.")
    else:
        print("Invalid BMI category.")

except ValueError:
    print("Invalid input. Please enter numeric values for weight and height.")
