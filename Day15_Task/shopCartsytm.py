

cart = []

prices = {
    "apple": 20,
    "banana": 10,
    "milk": 30,
    "bread": 40
}

try:
    n = int(input("How many items do you want? "))

    for i in range(n):
        item = input("Enter item name: ").lower()
        cart.append(item)

    #remove duplicates
    unique_cart = set(cart)

    total = 0

    for item in unique_cart:
        if item in prices:
            total += prices[item]
        else:
            print(item, "is not available")

    print("\nShopping Cart:", unique_cart)
    print("Total Cost:", total)

except ValueError:
    print("Invalid input! Enter a valid number.")