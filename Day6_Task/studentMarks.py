
# Student Marks Management System

subjects = ("Math", "Science", "English")
students = set()
student_data = {}

# Recursive function to calculate total marks
def calculate_total(marks):
    if len(marks) == 0:
        return 0
    return marks[0] + calculate_total(marks[1:])

# Function to add student
def add_student():
    name = input("Enter student name: ")

    if name in students:
        print("Student already exists.")
        return

    marks = []

    try:
        for subject in subjects:
            mark = float(input("Enter marks for " + subject + ": "))
            marks.append(mark)

        students.add(name)
        student_data[name] = marks
        print("Student added successfully.")

    except ValueError:
        print("Invalid input! Please enter numeric marks.")

# Function to display students
def display_students():
    if not student_data:
        print("No student records found.")
        return

    for name, marks in student_data.items():
        print(name, ":", marks)

# Function to calculate average
def calculate_average():
    try:
        name = input("Enter student name to calculate average: ")

        if name not in student_data:
            raise NameError

        marks = student_data[name]

        if not isinstance(marks, list):
            raise TypeError

        total = calculate_total(marks)
        average = total / len(marks)

        print("Total Marks:", total)
        print("Average Marks:", average)

    except NameError:
        print("Student name not found.")

    except ZeroDivisionError:
        print("Cannot divide by zero.")

    except TypeError:
        print("Marks data type error.")

# Main menu
while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Calculate Average")
    print("4. Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            add_student()

        elif choice == 2:
            display_students()

        elif choice == 3:
            calculate_average()

        elif choice == 4:
            print("Exiting program...")
            break

        else:
            print("Invalid choice!")

    except ValueError:
        print("Please enter a valid menu number.")
