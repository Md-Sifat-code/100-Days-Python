# Step 1: Create a 3x3 grid using a nested list
grid = [[" " for _ in range(3)] for _ in range(3)]

# Step 2: Take input from the user for the position
position = input("Enter the position of the treasure (e.g., 23 for column 2, row 3): ")

# Step 3: Convert the input into row and column indices
column = int(position[0]) - 1  # Subtract 1 to match zero-indexing
row = int(position[1]) - 1     # Subtract 1 to match zero-indexing

# Step 4: Place an "X" at the specified position
grid[row][column] = "X"

# Step 5: Print the updated grid
for row in grid:
    print(row)
