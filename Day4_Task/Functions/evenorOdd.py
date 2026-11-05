# Write a function to check whether a number is even or odd. 

def even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter a number: "))
print(even_odd(num))