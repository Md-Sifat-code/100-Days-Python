# User inputs
size = input("Enter pizza size (S, M, L): ")
add_pepperoni = input("Do you want pepperoni? (Y or N): ")
extra_cheese = input("Do you want extra cheese? (Y or N): ")

# Base prices
price = 0

if size == "S":
    price = 15
    if add_pepperoni == "Y":
        price += 2
elif size == "M":
    price = 20
    if add_pepperoni == "Y":
        price += 3
elif size == "L":
    price = 25
    if add_pepperoni == "Y":
        price += 3

# Add extra cheese if chosen
if extra_cheese == "Y":
    price += 1

# Final bill
print(f"Your final bill is: ${price}")
