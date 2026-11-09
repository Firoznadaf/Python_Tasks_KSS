"""Dictionary Sorting: Given a dictionary:
 python
students = { "Rahul": 85, "Amit": 92, "Priya": 78, "Sneha": 95 }
Sort the dictionary based on marks in descending order and print the top two students."""

students = { 
    "Rahul": 85,
    "Amit": 92,
    "Priya": 78,
    "Sneha": 95
}

# Sort based on marks in descending order
sorted_students = sorted(
    students.items(),
    key=lambda item: item[1],
    reverse=True
)

print("Students sorted by marks:")

for name, marks in sorted_students:
    print(name, ":", marks)

# Print top two students
print("\nTop two students:")

for name, marks in sorted_students[:2]:
    print(name, ":", marks)