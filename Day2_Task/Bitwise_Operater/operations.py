# Write a program to perform left shift (<<) and right shift (>>) operations on a number. 

num = int(input("Enter a number: "))
shift = int(input("Enter number of positions to shift: "))

left_shifted = num << shift
right_shifted = num >> shift

print(f"Left Shift ({num} << {shift}): {left_shifted}")
print(f"Right Shift ({num} >> {shift}): {right_shifted}")