# Small Shop Billing System

# Dictionary to store products and prices
products = {
    "Pen": 10,
    "Notebook": 50,
    "Pencil": 5
}

# Set to store product categories
categories = {"Stationery", "Writing", "Education"}

# Tuples to store product details
product_details = (
    ("Pen", 10, "Writing"),
    ("Notebook", 50, "Education"),
    ("Pencil", 5, "Writing")
)

# List to store cart items
cart = []

# Function to display products
def display_products():
    print("\nAvailable Products:")

    for name, price in products.items():
        print(name, ":", price)

# Function to add items to cart
def add_to_cart():
    try:
        name = input("Enter product name: ")

        if name not in products:
            raise NameError

        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            raise ValueError

        cart.append((name, quantity))
        print("Item added to cart successfully.")

    except ValueError:
        print("Invalid quantity! Please enter a number.")

    except NameError:
        print("Product not found in store.")

# Recursive function to calculate total price
def calculate_total(index=0):
    if index == len(cart):
        return 0

    name, quantity = cart[index]

    if not isinstance(name, str) or not isinstance(quantity, int):
        raise TypeError

    price = products[name] * quantity

    return price + calculate_total(index + 1)

# Function to calculate and display bill
def view_total_bill():
    try:
        if not cart:
            print("Cart is empty.")
            return

        print("\nItems in Cart:")

        for name, quantity in cart:
            print(name, "x", quantity)

        total = calculate_total()
        print("Total Bill:", total)

    except TypeError:
        print("Cart data type error.")

    except ZeroDivisionError:
        print("Calculation error: division by zero.")

# Main menu
while True:
    print("\n1. Display Products")
    print("2. Add Item to Cart")
    print("3. View Total Bill")
    print("4. Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            display_products()

        elif choice == 2:
            add_to_cart()

        elif choice == 3:
            view_total_bill()

        elif choice == 4:
            print("Thank you for shopping!")
            break

        else:
            print("Invalid choice!")

    except ValueError:
        print("Please enter a valid menu number.")
