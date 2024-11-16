def formate_name(f_name, l_name):
    # Capitalize the first letter of each word and make the rest lowercase
    # .title() ensures proper name formatting
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

# Example: "Sifat" and "js" are formatted to "Sifat Js" using .title()
print(formate_name("Sifat", "js"))
