def formate_name(f_name,l_name):
    if f_name == "" or l_name=="":
        return "Please Give some valid inputs"

    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"


print(formate_name(input("Enter your first name\n"),input("Enter last name\n")))