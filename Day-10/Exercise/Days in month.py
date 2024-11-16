

def leap(year):
    leapyear = year / 4
    if leapyear % 2 == 0:
        return True
    else:
        return False


def days_in_month(year,month):
    days_in_normal =[31,28,31,30,31,30,31,31,30,31,30,31]
    days_in_abnormal =[31,29,31,30,31,30,31,31,30,31,30,31]
    if leap(year):
        print(days_in_abnormal[int(month)-1])
    else:
        print((days_in_normal[int(month)-1]))


x = int(input("Enter the year: \n"))
y = int(input("Enter the month: \n"))
days_in_month(x,y)