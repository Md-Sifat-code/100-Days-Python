#Block Scope

game_lvl = 3
enemy = ["Zombie", "Skeletons", "Aliens"]
if game_lvl < 5:
    new_enemy = enemy[0]

print(new_enemy)
#Block scope mainly those variables which is called into the Loops, conditions
#As soon as you create an variable into a fucntion it will turn into an local scope variable