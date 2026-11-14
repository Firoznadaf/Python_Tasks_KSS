# Employee Salary Management System

employees = []

# read employee records
file = open("employees.txt", "r")

for line in file:
    name, salary = line.split()

    salary = int(salary)

    employees.append((name, salary))

file.close()

# display employee details
print("Employee details:")

for name, salary in employees:
    print(name, salary)

# find highest salary
if len(employees) > 0:
    highest = max(employees, key=lambda x: x[1])

    print("\nHighest paid Employee:")
    print("Name:", highest[0])
    print("Salary:", highest[1])
else:
    print("No employee records found.")

# add new employee
name = input("\nEnter employee name: ")
salary = int(input("Enter employee salary: "))

file = open("employees.txt", "a")

file.write(name + " " + str(salary) + "\n")

file.close()

print("Employee added successfully")