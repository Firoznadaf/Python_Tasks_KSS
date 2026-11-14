import os

# get the folder where the Python program is saved
folder = os.path.dirname(os.path.abspath(__file__))

# create the file path
file_path = os.path.join(folder, "attendance.txt")

name = input("Enter student name: ")

# write attendance
with open(file_path, "a") as file:
    file.write(name + "\n")

# read attendance
with open(file_path, "r") as file:
    print("\nAttendance Records:")
    print(file.read())