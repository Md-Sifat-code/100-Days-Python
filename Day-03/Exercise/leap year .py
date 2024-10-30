x = int(input("Enter the year: \n"))

leapyear = x/4
if leapyear%2 ==0:
    print("This is a leap year")
else:
    print("This is not a leap year")