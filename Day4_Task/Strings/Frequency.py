# Write a program to count the frequency of each character in a string. 

str1 = input("Enter a string: ")

for ch in set(str1):
    print(ch, ":", str1.count(ch))