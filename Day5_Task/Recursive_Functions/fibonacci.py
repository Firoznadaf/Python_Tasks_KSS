# Write a recursive function to find the nth Fibonacci number. 

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

num = int(input("Enter a number: "))
print("Fibonacci:", fibo(num))