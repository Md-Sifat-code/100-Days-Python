from random import choice

word_list = ["Avengers","Mother", "IceBurg"]
choosen_word = choice(word_list).lower()
print(choosen_word)
guess_word = input("Enter your letter: \n").lower()
print(guess_word)

for letter in choosen_word:
    if guess_word == letter:
        print("got it")
    else:
        print("Wrong")


# in this challange -01 we just need to choice an word from a list . and user will get an chnance to guess an letter for the word . then we used in keyword to check the letter that use
# give i in the word that randomly choosen
# This is how the