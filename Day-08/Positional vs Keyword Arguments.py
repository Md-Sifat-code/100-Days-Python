# Function with positional, keyword, and default arguments
def introduce(name, age, city="Unknown"):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")

# Using positional arguments
introduce("Alice", 30)

# Using keyword arguments
introduce(age=25, name="Bob", city="New York")

# Mixing positional and keyword arguments
introduce("Charlie", age=22)

# Keyword argument with a default value used
introduce("Dana", 28)
