import calculator

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\n1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Result:", calculator.addition(num1, num2))

elif choice == 2:
    print("Result:", calculator.subtraction(num1, num2))

elif choice == 3:
    print("Result:", calculator.multiplication(num1, num2))

elif choice == 4:
    print("Result:", calculator.division(num1, num2))

else:
    print("Invalid choice!")
