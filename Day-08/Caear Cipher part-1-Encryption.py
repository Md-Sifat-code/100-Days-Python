from art import logo
print(logo)


alphabet =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ,'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




def encrypt(plain_text,number):
    cipher_text =""
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + number
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text+=letter
    print(f"The encoded text is {cipher_text}")


def decrypt(plain_text,number):
    cipher_text =""
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position - number
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text += letter
    print(f"The decoded text is {cipher_text}")



while True:
    want = input("You want to play?\n")
    if want !="yes":
        print("Good Bye. Hope you play again")
    else:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number :\n"))
        shift = shift % 26
        to_do = input("Which typer you want to do?\n")
        if to_do == "decode":
            decrypt(text, shift)
        elif to_do == "encode":
            encrypt(text, shift)
