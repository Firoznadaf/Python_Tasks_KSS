# Write a program to check whether a string is a palindrome. 

str1 = input("Enter a string: ")

if str1 == str1[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")