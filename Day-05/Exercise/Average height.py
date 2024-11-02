students_height = [180,124,165,173,189,169,146]
sum_of_height = 0
for height in students_height:
    sum_of_height+=height

total = sum_of_height / len(students_height)
print(f"The average height is:{total:.2f}")