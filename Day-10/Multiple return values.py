def formate_name(f_name, l_name):
    # Check if either first name or last name is an empty string
    # If any input is empty, return an error message
    if f_name == "" or l_name == "":
        return "Please Give some valid inputs"

    # Capitalize the first letter of each word and make the rest lowercase
    # This ensures the names are formatted correctly
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    # Return the formatted name with a "Result:" prefix for clarity
    return f"Result: {formated_f_name} {formated_l_name}"

# Prompt the user for their first and last name
# The inputs are passed to the formate_name function
print(formate_name(input("Enter your first name\n"), input("Enter last name\n")))
