# University Staff Management (Hierarchical Inheritance) 

class Staff:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Professor(Staff):
    def display(self):
        print("Professor:", self.name, self.salary)

class LabAssistant(Staff):
    def display(self):
        print("Lab Assistant:", self.name, self.salary)

class Administrator(Staff):
    def display(self):
        print("Administartor:", self.name, self.salary)

p = Professor("Firoz", 60000)
l = LabAssistant("Irannagouda", 30000)
a = Administrator("Priya", 40000)

p.display()
l.display()
a.display()