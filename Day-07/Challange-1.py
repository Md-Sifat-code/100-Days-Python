from random import choice

word_list = ["Avengers"," Mother", "IceBurg"]
choosen_word = choice(word_list)
choosen_word.lower()
print(choosen_word)
guess_word = input("Enter your letter: \n")
guess_word.lower()

if guess_word in choosen_word:
    print("got it")

# in this challange -01 we just need to choice an word from a list . and user will get an chnance to guess an letter for the word . then we used in keyword to check the letter that use
# give i in the word that randomly choosen
# This is how the