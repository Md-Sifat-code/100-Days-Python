# A while loop in Python is used to repeatedly execute a block of code
# as long as a specified condition is True.

# Syntax:
# while <condition>:
#     # code to execute

# Explanation:
# 1. The condition is evaluated at the beginning of each iteration.
# 2. If the condition is True, the loop’s code block executes.
# 3. After each execution of the code block, the condition is re-evaluated.
# 4. The loop stops when the condition becomes False.

# Example:
count = 3  # Initializing a variable

while count > 0:  # Condition is checked at the start of each loop
    print("Counting down:", count)  # This line runs as long as count > 0
    count -= 1  # Decrement count by 1 after each iteration

# How it works:
# - Initially, count is 3, so the condition (count > 0) is True, and the loop runs.
# - count is then decreased by 1 each time.
# - When count becomes 0, the condition (count > 0) is False, so the loop stops.

# Key Points:
# - The `while` loop runs as long as the condition is True.
# - Make sure to update variables inside the loop; otherwise, you might create an infinite loop.
