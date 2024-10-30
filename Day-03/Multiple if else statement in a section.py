print("Welcome to the amusement park!")
print("We have the following rides:")
print("1. Roller Coaster - $10")
print("2. Ferris Wheel - $7")
print("3. Bumper Cars - $5")

# Ask user for their choice of ride
ride_choice = input("Which ride would you like to take? (roller_coaster, ferris_wheel, bumper_cars): ").strip().lower()

# Initialize bill
bill = 0

# Determine the cost of the chosen ride using conditional statements
if ride_choice == "roller_coaster":
    bill = 10
elif ride_choice == "ferris_wheel":
    bill = 7
elif ride_choice == "bumper_cars":
    bill = 5

    # Ask if the user wants a photo
    photo_choice = input("Would you like to take a photo during the ride? (y/n): ").strip().lower()

    # Add photo cost if the user wants a photo
    if photo_choice == 'y':
        bill += 3

else:
    print("Invalid choice. Please select a valid ride.")
    exit()

# Print the final bill
print(f"Your final bill is: ${bill}")
