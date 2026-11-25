

import random

# generate 10 random num
numbers = []

for i in range(10):
    numbers.append(random.randint(1, 100))

print("Random Numbers:", numbers)

even = 0
odd = 0

# count even and odd num
for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even Numbers:", even)
print("Odd Numbers:", odd)

# remove duplicates using set
unique_numbers = set(numbers)

print("Unique Numbers:", unique_numbers)