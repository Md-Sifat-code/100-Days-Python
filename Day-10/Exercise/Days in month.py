# Function to check if a given year is a leap year
def leap(year):
    # Incorrect logic: divides the year by 4 and checks if the result is divisible by 2
    leapyear = year / 4
    if leapyear % 2 == 0:
        return True  # Returns True if the year is considered a leap year
    else:
        return False  # Returns False otherwise


# Function to determine the number of days in a given month of a specific year
def days_in_month(year, month):
    # List of days in each month for a normal (non-leap) year
    days_in_normal = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # List of days in each month for a leap year
    days_in_abnormal = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Check if the year is a leap year using the leap() function
    if leap(year):
        # If it is a leap year, print the number of days from the leap year list
        print(days_in_abnormal[int(month) - 1])
    else:
        # If it is not a leap year, print the number of days from the normal year list
        print(days_in_normal[int(month) - 1])


# Taking input from the user for year and month
x = int(input("Enter the year: \n"))  # Input year
y = int(input("Enter the month: \n"))  # Input month (1-12)

# Calling the days_in_month function with user inputs
days_in_month(x, y)
