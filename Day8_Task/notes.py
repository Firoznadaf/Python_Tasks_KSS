# Notes Reader Program 

# open notes file in read mode
file = open("notes1.txt","r")

# read all contents
content = file.read()

# Display contents
print("Daily Notes:")
print(content)

file.close()