import random

# Define the character lists
alphabets = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
    '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/',
    '~', '`'
]

def generate_password():
    # Get user input for the number of each type of character
    num_alphabets = int(input("Enter the number of alphabets: "))
    num_numbers = int(input("Enter the number of numbers: "))
    num_symbols = int(input("Enter the number of symbols: "))

    # Generate the password components
    chosen_alphabets = random.choices(alphabets, k=num_alphabets)
    chosen_numbers = random.choices(numbers, k=num_numbers)
    chosen_symbols = random.choices(symbols, k=num_symbols)

    # Combine all components
    password_list = chosen_alphabets + chosen_numbers + chosen_symbols

    # Shuffle the list to randomize order
    random.shuffle(password_list)

    # Join into a single string for the final password
    password = ''.join(password_list)
    return password

# Generate and print the password
print("Generated Password:", generate_password())
