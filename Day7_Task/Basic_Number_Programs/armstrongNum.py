# Write a program to check whether a given number is an Armstrong number or not.

num = int(input("Enter a number: "))
temp = num
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit ** 3
    num = num // 10

if sum == temp:
    print(temp, "is an Armstrong number")
else:
    print(temp, "is not an Armstrong number")