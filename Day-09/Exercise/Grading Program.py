studetns_numbers ={
    "Harry" : 81,
    "Ron" : 78,
    "Hermione" : 99,
    "Draco": 74,
    "Neville" :62

}

for x in studetns_numbers:
    number = studetns_numbers[x]
    if number>90:
        print("Outstanding ")
    elif number > 80 and number <=90:
        print("Exceeds Expectations")
    elif number>70 and number<= 80:
        print("Acceptable")
    else:
        print("Fail")