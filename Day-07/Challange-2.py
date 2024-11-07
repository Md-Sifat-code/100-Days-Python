from random import choice

word_list = ["Avengers","Mother", "IceBurg","keep"]
chosen_word = choice(word_list).lower()
empty_list =[]
empty_list.extend(["_"]*len(chosen_word))
print(empty_list)
guess_word = input("Enter your letter: \n").lower()
number =0
for letter in chosen_word:
    if guess_word == letter:
        print("got it")
        empty_list[number]= letter
    else:
        print("Wrong")

    number +=1

print(empty_list)

for x in empty_list:
    print(x, end="")  # This will print each item without a newline
print()  # Print a newline at the end

# Another way of printing in same line is: print("".join(empty_list))  # Joins all items in the list as a single string