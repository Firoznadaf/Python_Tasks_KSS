"""List of Dictionaries: Given the following data:
python
    employees = [
        {"name": "John", "age": 25, "salary": 30000},
        {"name": "Alice", "age": 30, "salary": 50000},
        {"name": "Bob", "age": 28, "salary": 40000},
        {"name": "David", "age": 35, "salary": 60000}]
    Perform the following:
    * Find the employee with the highest salary.
    * Filter employees whose salary is greater than 35,000.
    * Calculate the average salary.
    * Create a list containing only employee names."""

employees = [
     {"name": "John", "age": 25, "salary": 30000},
    {"name": "Alice", "age": 30, "salary": 50000},
    {"name": "Bob", "age": 28, "salary": 40000},
    {"name": "David", "age": 35, "salary": 60000}
]

# 1. Employee with highet salary

highest = max(employees, key=lambda emp: emp["salary"])

print("Employee with highest salary:")
print(highest)

# 2. Employees with salary greter than 35000
filtered = []
for emp in employees:
    if emp["salary"] > 35000:
        filtered.append(emp)

print("\nEmployees with salary greter than 35000:")

for emp in filtered:
    print(emp)

# 3. Calculate average salary
total_salary = 0

for emp in employees:
    total_salary += emp["salary"]

average = total_salary / len(employees)

print("\nAverage salary:", average)

# 4. Create a list containing employee names
names = []

for emp in employees:
    names.append(emp["name"])

print("\nEmployee names:", names)