height = float(input("Enter your height in cm: \n"))
weight = float(input("Enter your weight in kg: \n"))

# Convert height from cm to meters for BMI calculation
height = height / 100

# Calculate BMI
BMI = weight / (height * height)

# Check BMI categories
if BMI <= 18.5:
    print("You are underweight")
elif 18.5 < BMI < 25.0:
    print("Your weight is normal")
elif 25.0 <= BMI < 30.0:
    print("You are overweight")
elif 30.0 <= BMI < 35.0:
    print("You are obese")
else:
    print("You are clinically obese")
