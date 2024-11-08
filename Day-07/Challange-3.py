from random import choice

word_list = ["Avengers", "Mother", "IceBurg", "keep"]
chosen_word = choice(word_list).lower()
empty_list = ["_"] * len(chosen_word)  # Initializes the hidden word with underscores
player_life = 7
print(empty_list)

while "_" in empty_list:
    if player_life > 0:
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
            player_life -= 1

        print(empty_list)
    else:
        print("You don't have any life left to guess the letter.")
        break  # Exit the loop if no lives are left

# Check if the player won or lost
if "_" not in empty_list:
    print("Congratulations! The word is:", "".join(empty_list))
else:
    print("Game Over! The word was:", chosen_word)
