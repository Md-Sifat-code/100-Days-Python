alphabet =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ,'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


text = input("Type your message:\n").lower()
shift = int(input("Type the shift number :\n"))

def encrypt(plain_text,number):
    cipher_text =""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + number
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")


def decrypt(plain_text,number):
    cipher_text =""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position - number
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The decoded text is {cipher_text}")


decrypt(text,shift)
encrypt(text,shift)