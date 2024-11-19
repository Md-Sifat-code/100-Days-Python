# Difference Between print and return in Python

# Example 1: Using print
def greet_with_print(name):
    """
    This function uses print to display the greeting.
    The output is shown in the console, but it cannot be reused in the program.
    """
    print(f"Hello, {name}!")  # Displays the greeting in the console

# Calling the function
greet_with_print("Alice")
# Output: Hello, Alice!

# Note: The above function does not return anything, so we cannot store or reuse the output.

# Example 2: Using return
def greet_with_return(name):
    """
    This function uses return to send the greeting back to the caller.
    The returned value can be stored and reused in the program.
    """
    return f"Hello, {name}!"  # Sends the greeting back to the caller

# Calling the function and storing the returned value in a variable
greeting = greet_with_return("Bob")
print(greeting)  # Output: Hello, Bob!

# Example 3: Why return is more flexible
def add_numbers(a, b):
    """
    This function returns the sum of two numbers.
    The returned result can be reused in other calculations.
    """
    return a + b

# Using the return value in further calculations
sum1 = add_numbers(5, 10)  # Returns 15
sum2 = add_numbers(sum1, 20)  # Uses the previous result and returns 35
print(f"The final result is: {sum2}")
# Output: The final result is: 35

# Example 4: Why print is less flexible
def add_numbers_with_print(a, b):
    """
    This function prints the sum of two numbers.
    The result cannot be reused or stored.
    """
    print(f"The sum is: {a + b}")  # Only displays the result

# Trying to reuse the result (but it's not possible with print)
result = add_numbers_with_print(5, 10)  # Prints "The sum is: 15"
print(f"Result is: {result}")  # Output: Result is: None

# Note: Since the function uses print, the result is not returned to the caller. Instead, `result` is None.
