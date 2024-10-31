import random

# 1. Generate a random float between 0 and 1
# This will output a floating-point number from 0.0 up to but not including 1.0.
print("Random float between 0 and 1:", random.random())

# 2. Generate a random integer between 1 and 10 (inclusive)
# randint(a, b) generates an integer between 'a' and 'b', inclusive of both.
print("Random integer between 1 and 10:", random.randint(1, 10))

# 3. Choose a random element from a list
# choice(seq) selects a random item from a non-empty sequence, such as a list, tuple, or string.
fruits = ['apple', 'banana', 'cherry']
print("Random choice from list:", random.choice(fruits))

# 4. Generate a random float between 1.5 and 5.5
# uniform(a, b) generates a floating-point number between 'a' and 'b'.
print("Random float between 1.5 and 5.5:", random.uniform(1.5, 5.5))

# 5. Generate a random sample of 2 unique elements from a list
# sample(population, k) returns a list of 'k' unique elements chosen randomly from 'population'.
print("Random sample of 2 fruits:", random.sample(fruits, 2))

# 6. Shuffle the elements of a list in place
# shuffle(seq) randomly reorders the elements of a mutable sequence, such as a list.
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print("Shuffled list:", numbers)

# 7. Generate a random number from a range with a specific step
# randrange(start, stop, step) generates a random number within a range, with an optional step.
print("Random even number between 0 and 10:", random.randrange(0, 10, 2))
