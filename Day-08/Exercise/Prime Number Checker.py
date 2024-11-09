def prime_checker(number):
    if number <= 1:  # Numbers less than or equal to 1 are not prime
        return f"This {number} is not prime"

    # Check divisibility from 2 to the number - 1
    for x in range(2, number):
        if number % x == 0:
            return f"This {number} is not prime"

    return f"This {number} is prime"


# Prompt user for input and check if the number is prime
print(prime_checker(int(input("Enter the number you want to check:\n"))))
