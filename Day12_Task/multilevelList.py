#  Multi-Level List Transformation (Advanced List Comprehension) 

data = [[1, 2, 3], [4, 5], [6]]

flat = [x for row in data for x in row]

print("Flattened List:", flat)

squares = [x**2 for x in flat if x % 2 == 0]

print("Squares of Even Numbers:", squares)