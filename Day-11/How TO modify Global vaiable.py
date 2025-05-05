total_enemy =1
def increaseenemy():
    global total_enemy
    total_enemy+=1
    print(total_enemy)

increaseenemy()
#to update the global state variable from a function we need to use global as key