from random import choice

x = input("Heads or Tails? ")

y = ['Heads', 'Tails']
select_random = choice(y)  # randomly select 'Heads' or 'Tails'

if x == select_random:
    print(f"You got {x}. Congratulations!")
else:
    print(f"Sorry, it was {select_random}. Better luck next time!")
