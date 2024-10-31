import re

x = input("Enter his name ")
x.lower()
y = input("Enter her name")
y.lower()
part1 = re.split("[true]",x)
part2 = re.split("[true]",y)
total_true = (len(x)-len(part1))+( len(y)-len(part2))
part3 = re.split("[love]",x)
part4 = re.split("[love]",y)
total_love = (len(x)-len(part3))+ (len(x)-len(part3))
total = str(total_true)+str(total_love)
total_num = int(total)
if total_num <10 or total_num>90:
    print("you go together like coke and mentos")
elif 40<total_num<50:
    print("You are alright together")
else:
    print(f"your score is {total_num}")