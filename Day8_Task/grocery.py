#  Grocery List Manager

n = int(input("How many grocery items? "))

# create and open file in write mode
file = open("grocery.txt", "w")

for i in range(n):
    item = input("Enter grocery item: ")
    file.write(item + "\n")

file.close()

# display grocery list
file = open("grocery.txt", "r")

print("\nGrocery List:")
print(file.read())

file.close()