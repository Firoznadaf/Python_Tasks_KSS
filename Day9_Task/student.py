# Student Information System (Class & Object)

class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Marks:", self.marks)
        print()

s1 = Student("Firoz", 101, 85)
s2 = Student("Akshay", 102, 90)
s3 = Student("Kasim", 103, 78)

s1.display()
s2.display()
s3.display()