ascii_art = """
                              ,;;;;;;,
                            ,;;;;;;;;;;,
                           ;;;;;;;;;;;;;;
                   ==     ;;;;;;;;;;;;;;;     ==
                  ===;    ;;;;;;;;;;;;;;;    ;===
                =======   ;;;;;;;;;;;;;;;   =======
              =========.,,;;;;;;;;;;;;;;;,,=========
             ====================="====================
              ===================;;====================
                .================;================.
                   .===========;;;;;;===========.
                        .===========,===========.
                             .========,========.
                                 .====,====.
                                     .==.
"""

print(ascii_art)

# Extra function to clear the console
import os

def clear_console():
    os.system('cls')  # Clear console for Windows

# clear_console()  # Call this function to clear the console
auction_dictionary={}
while True:
    user = input("Enter your Name:\n")
    bid = int(input("Enter your Bid:\n"))
    x = input("Is there more person in the Auction with you?")
    if x =="yes":
        auction_dictionary[user] = bid
        clear_console()
    else:
        auction_dictionary[user] = bid
        break
lister =[]
for y in auction_dictionary:
    print(y)
    print(auction_dictionary[y])
    lister.append(auction_dictionary[y])

lister.sort()
for z in auction_dictionary:
    if auction_dictionary[z] == lister[-1]:
        print(f"The winner is {z}")