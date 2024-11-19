# Docstring Example in Python

# A docstring is a special string written in triple quotes (""" or ''').
# It is used to document a module, class, function, or method.
# Docstrings help developers understand what the code is intended to do.

# Example 1: Docstring for a Function
def add_numbers(a, b):
    """
    This function adds two numbers and returns the result.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The sum of the two numbers.
    """
    return a + b


# The docstring explains the purpose, parameters, and return value of the function.

# Example 2: Docstring for a Class
class Person:
    """
    A class to represent a person.

    Attributes:
    name (str): The name of the person.
    age (int): The age of the person.
    """

    def __init__(self, name, age):
        """
        Initializes the Person object with a name and age.

        Parameters:
        name (str): The name of the person.
        age (int): The age of the person.
        """
        self.name = name
        self.age = age

    def greet(self):
        """
        Prints a greeting message including the person's name.
        """
        print(f"Hello, my name is {self.name}!")


# Example 3: Docstring for a Module
"""
This module demonstrates the use of docstrings in Python.

It includes examples for documenting functions, classes, and modules.
"""

# Example usage
if __name__ == "__main__":
    # Using the add_numbers function
    result = add_numbers(5, 10)
    print(f"Sum: {result}")  # Output: Sum: 15

    # Using the Person class
    person = Person("Alice", 25)
    person.greet()  # Output: Hello, my name is Alice!
