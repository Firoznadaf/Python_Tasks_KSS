# Write a program to check whether a number is a Palindrome. 

num = int(input("Enter a number: "))
temp = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if temp == rev:
    print(temp, "is a Palindrome number")
else:
    print(temp, "is not a Palindrome number")