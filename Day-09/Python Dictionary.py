programming_dictionary = {
    "Bug" : "An Error in a program that prevents the program from running as expected",
    "Function":"A piece of code that you can easily call over and over again",

}
# This is called dictionary in python similar to the java script object. In here we can find a key along with it's values
#  In here we can see "Bug" is one of the key of this dictionary and it has a value of  "An Error in a program that prevents the program from running as expected"


# How to print an key values from an dictionary
print(programming_dictionary["Function"])
# Adding new items to dictionary
programming_dictionary["Loop"] = "Loop is like doing a thing over and over"
# an empty dictionary look like
empty_dictionary ={}
# wipe out an existing dictionary
programming_dictionary = {}
# Loop through a dictionary
for key in programming_dictionary:
    print(key)#this one will print the key
    print(programming_dictionary[key]) #this will print the values