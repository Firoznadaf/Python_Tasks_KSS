# Write a program to check whether a given number is a Strong number.

num = int(input("Enter a number: "))
temp = num
sum = 0

while num > 0:
    digit = num % 10
    fact = 1

    for i in range(1, digit + 1):
        fact = fact * i

    sum = sum + fact
    num = num // 10

if sum == temp:
    print(temp, "is a Strong number")
else:
    print(temp, "is not a Strong number")