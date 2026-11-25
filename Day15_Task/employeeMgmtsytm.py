

import os

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)

employees = {}

try:
    n = int(input("Enter number of employee:"))

    for i in range(n):
        name = input("\nEnter employee name: ")

        try:
            salary = float(input("Enter salary: "))

            if salary < 0:
                raise ValueError("Salary cannot be negative")

            employees[name] = Employee(name, salary)

        except ValueError as e:
            print("Invalid salary:", e)

    # display employee
    print("\nEmployee Details")

    for name, emp in employees.items():
        emp.display()
        print()

    # save to file
    folder_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(folder_path, "employees.txt")

    with open(file_path, "w") as file:
        for name, emp in employees.items():
            file.write(f"{name}: {emp.salary}\n")

    print("Employee data saved!")

except ValueError:
    print("Please enter a valid employee count.")

except IOError:
    print("File error occurred.")