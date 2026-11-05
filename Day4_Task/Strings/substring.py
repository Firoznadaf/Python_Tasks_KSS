# Write a program to check whether a substring exists in a string. 

str1 = input("Enter a string: ")
sub = input("Enter substring to search: ")

if sub in str1:
    print("Substring exists")
else:
    print("Substring does not exist")
