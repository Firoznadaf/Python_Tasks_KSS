# Student Attendance Record 

name = input("Enter student name: ")

# file open append mode
file = open("attendance.txt", "a")

# write a student name
file.write(name + "\n")

file.close()

# Read and display the file
file = open("attendance.txt", "r")

print("\nAttendance Records:")
print(file.read())