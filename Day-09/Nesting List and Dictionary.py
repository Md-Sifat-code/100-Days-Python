# Nested listing refers to the concept of having lists within other lists. 
# This allows us to create complex structures where each item in a list could 
# be another list containing more elements.

# Example of a nested list:
nested_list = [
    ["apple", "banana"],  # This is the first list within the main list.
    ["carrot", "pea"],    # This is the second list within the main list.
    ["bread", "butter"]   # This is the third list within the main list.
]

# Accessing elements in a nested list:
# For instance, to access "banana", you would write:
print(nested_list[0][1])  # Output: "banana"

# Nested dictionaries refer to having dictionaries within other dictionaries. 
# This enables storing more detailed and complex data structures by having each 
# key in a dictionary map to another dictionary, which can hold further information.

# Example of a nested dictionary:
travel_log = [
    {
        "country": "Bangladesh",                # First dictionary in the list
        "cities_visited": ["Paris", "Lille", "Dijon"],  # Nested list within dictionary
        "total_visits": 12
    },
    {
        "country": "France",                    # Second dictionary in the list
        "cities_visited": ["Berlin", "West Ham", "Brasil", "Portugal"],
        "total_visits": 5
    }
]

# Accessing elements in a nested dictionary:
# To access the list of cities visited in Bangladesh, you would write:
print(travel_log[0]["cities_visited"])  # Output: ["Paris", "Lille", "Dijon"]

# To get the total visits to France:
print(travel_log[1]["total_visits"])    # Output: 5

# In this example, `travel_log` is a list that contains dictionaries. Each dictionary
# represents a country with keys such as "country", "cities_visited", and "total_visits".
# The "cities_visited" key has a nested list to store multiple cities visited in that country.
