print("Welcome to the tip calculator!!")
x = float(input("Enter the total bill: \n"))
z = float(input("How many people are there? \n"))
y = float(input("Enter the percentage you guys want to give as tip: \n"))/100

print(f"Each Person have to pay {((x/z)*(1+y)):.2f}")