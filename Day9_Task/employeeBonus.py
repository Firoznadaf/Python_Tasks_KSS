#  Employee Bonus Calculator (Decorators & OOP) 

def bonus(func):
    def wrapper(self):
        self.salary += self.salary * 0.10
        func(self)
    return wrapper

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @bonus
    def display(self):
        print("Employee Name:", self.name)
        print("Salary with Bonus:", self.salary)

e = Employee("Rahul", 30000)
e.display()