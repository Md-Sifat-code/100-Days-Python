# 1. Initialization
my_list = []          # Empty list
my_list = [1, 2, 3]   # List with elements

# 2. Adding Elements
my_list.append(4)           # Adds 4 to the end: [1, 2, 3, 4]
my_list.insert(1, 5)        # Inserts 5 at index 1: [1, 5, 2, 3, 4]

# 3. Removing Elements
my_list.pop()               # Removes last element: [1, 5, 2, 3]
my_list.pop(1)              # Removes element at index 1: [1, 2, 3]
my_list.remove(2)           # Removes first occurrence of 2: [1, 3]

# 4. Accessing Elements
first_element = my_list[0]                 # Accesses the first element: 1
sublist = my_list[0:2]                     # Slices the list: [1, 3]

# 5. Searching
index_of_3 = my_list.index(3)              # Finds the index of 3: 1
is_present = 3 in my_list                  # Checks if 3 is in the list: True

# 6. Modifying Elements
my_list[0] = 10                            # Updates index 0 to 10: [10, 3]

# 7. Sorting and Reversing
my_list = [3, 1, 4, 1, 5]
my_list.sort()                             # Sorts in ascending order: [1, 1, 3, 4, 5]
my_list.sort(reverse=True)                 # Sorts in descending order: [5, 4, 3, 1, 1]
my_list.reverse()                          # Reverses the list: [1, 1, 3, 4, 5]

# 8. List Length
length = len(my_list)                      # Gets the length of the list: 5

# 9. Memory-Efficient Operations
my_list.clear()                            # Clears all elements: []
my_list = [1, 2, 3]
copy_list = my_list.copy()                 # Creates a shallow copy: [1, 2, 3]
my_list.extend([4, 5])                     # Extends list with another list: [1, 2, 3, 4, 5]

# 10. List Comprehensions
squared = [x ** 2 for x in my_list if x > 2]  # Squares elements greater than 2: [9, 16, 25]
