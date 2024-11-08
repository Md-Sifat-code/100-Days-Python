from random import choice

word_list = ["Avengers", "Mother", "IceBurg", "keep"]
chosen_word = choice(word_list).lower()
empty_list = ["_"] * len(chosen_word)  # Initializes the hidden word with underscores

print(empty_list)

while "_" in empty_list:
    guess_letter = input("Enter your letter: \n").lower()
    found = False  # Flag to check if the letter is found

    # Check if the guessed letter is in the chosen word
    for index, letter in enumerate(chosen_word):
        if guess_letter == letter:
            empty_list[index] = letter  # Replace the underscore with the correct letter
            found = True

    if found:
        print("Got it!")
    else:
        print("Wrong")

    print(empty_list)

# Print the final result
print("Congratulations! The word is:", "".join(empty_list))

for x in empty_list:
    print(x, end="")  # This will print each item without a newline
print()  # Print a newline at the end

# Another way of printing in same line is: print("".join(empty_list))  # Joins all items in the list as a single string