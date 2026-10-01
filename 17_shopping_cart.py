#Shopping Cart using Functions
cart = []
def add_item():
    """Function to add an item to the shopping cart."""
    item = input("Enter the item to add: ")
    cart.append(item)
    print(f"{item} has been added to the cart.")
def remove_item():
    """Function to remove an item from the shopping cart."""    
    item = input("Enter the item to remove: ")
    if item in cart:
        cart.remove(item)
        print(f"{item} has been removed from the cart.")
    else:
        print(f"{item} is not in the cart.")
def view_cart():
    """Function to view the items in the shopping cart."""
    if cart:
        print("Items in the cart:")
        for item in cart:
            print(f"-> {item}")
    else:
        print("The cart is empty.")
def calculate_total():
    """Function to calculate the total cost of items in the shopping cart."""
    total = len(cart) * 50
    print(f"The total cost of items in the cart is: ${total}")
def checkout():
    """Function to checkout and calculate the total cost."""
    calculate_total()
    print("Thank you for shopping with us!")
print("Welcome to my Shopping Cart! Please select an option:")
print("1. Add item")
print("2. Remove item")
print("3. View cart")
print("4. Calculate total")
print("5. Checkout")
print("6. Exit")
while True:
    choice = input("Enter your choice (1-6): ")
    if choice == '1':
        add_item()
    elif choice == '2':
        remove_item()
    elif choice == '3':
        view_cart()
    elif choice == '4':
        calculate_total()
    elif choice == '5':
        checkout()
        break
    elif choice == '6':
        print("Exiting the shopping cart. Thank you for shopping with us!")
        break
    else:
        print("Invalid choice. Please try again.")