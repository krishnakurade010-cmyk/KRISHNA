# ShopCart - Shopping Cart System

products = {
    "Laptop": 55000,
    "Smartphone": 25000,
    "Headphones": 2000,
    "Smart Watch": 3500,
    "Keyboard": 1200,
    "Mouse": 800
}

cart = {}


def show_products():
    print("\n===== OUR PRODUCTS =====")

    for name, price in products.items():
        print(name, "- ₹", price)


def add_to_cart():
    show_products()

    name = input("\nEnter product name: ")

    if name in products:
        if name in cart:
            cart[name] += 1
        else:
            cart[name] = 1

        print(name, "added to cart!")
    else:
        print("Product not found.")


def show_cart():
    print("\n===== SHOPPING CART =====")

    if not cart:
        print("Your cart is empty.")
        return

    total = 0

    for name, quantity in cart.items():
        price = products[name]
        subtotal = price * quantity

        print(name)
        print("Price: ₹", price)
        print("Quantity:", quantity)
        print("Subtotal: ₹", subtotal)
        print("--------------------")

        total += subtotal

    print("Total: ₹", total)


def remove_from_cart():
    if not cart:
        print("\nYour cart is empty.")
        return

    show_cart()

    name = input("\nEnter product name to remove: ")

    if name in cart:
        del cart[name]
        print(name, "removed from cart!")
    else:
        print("Product not found in cart.")


def checkout():
    if not cart:
        print("\nYour cart is empty!")
        return

    show_cart()

    print("\n===== CHECKOUT =====")

    name = input("Enter your name: ")
    email = input("Enter your email: ")
    mobile = input("Enter mobile number: ")
    address = input("Enter delivery address: ")

    print("\nPayment Method:")
    print("1. Cash on Delivery")
    print("2. UPI")
    print("3. Debit Card")
    print("4. Credit Card")

    payment = input("Choose payment method: ")

    print("\n🎉 Order placed successfully!")
    print("Thank you,", name)

    cart.clear()


while True:

    print("\n========================")
    print("       🛒 SHOPCART")
    print("========================")

    print("1. Show Products")
    print("2. Add to Cart")
    print("3. Show Cart")
    print("4. Remove from Cart")
    print("5. Checkout")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        show_products()

    elif choice == "2":
        add_to_cart()

    elif choice == "3":
        show_cart()

    elif choice == "4":
        remove_from_cart()

    elif choice == "5":
        checkout()

    elif choice == "6":
        print("Thank you for using ShopCart!")
        break

    else:
        print("Invalid choice. Please try again.")

