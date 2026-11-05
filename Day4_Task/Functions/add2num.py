#  Write a program using a user-defined function to add two numbers. 

def add(a, b):
    return a + b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum:", add(num1, num2))