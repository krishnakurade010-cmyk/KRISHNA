from flask import Flask, render_template, redirect, url_for, request
import sqlite3

app = Flask(__name__)

# =========================
# PRODUCTS
# =========================
products = {
    "Laptop": {
        "price": 55000,
        "category": "Electronics",
        "icon": "💻"
    },
    "Smartphone": {
        "price": 25000,
        "category": "Electronics",
        "icon": "📱"
    },
    "Headphones": {
        "price": 2000,
        "category": "Accessories",
        "icon": "🎧"
    },
    "Smart Watch": {
        "price": 3500,
        "category": "Accessories",
        "icon": "⌚"
    },
    "Keyboard": {
        "price": 1200,
        "category": "Accessories",
        "icon": "⌨️"
    },
    "Mouse": {
        "price": 800,
        "category": "Accessories",
        "icon": "🖱️"
    }
}

# =========================
# CART
# =========================
cart = {}


# =========================
# DATABASE
# =========================
def create_database():
    connection = sqlite3.connect("shopcart.db")

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            email TEXT NOT NULL,
            mobile TEXT NOT NULL,
            address TEXT NOT NULL,
            payment_method TEXT NOT NULL,
            total_amount REAL NOT NULL
        )
    """)

    connection.commit()
    connection.close()


# =========================
# CART TOTAL
# =========================
def get_cart_total():
    total = 0

    for name, quantity in cart.items():
        total += products[name]["price"] * quantity

    return total


# =========================
# CART COUNT
# =========================
def get_cart_count():
    return sum(cart.values())


# =========================
# HOME
# =========================
@app.route("/")
def home():

    cart_items = []

    for name, quantity in cart.items():

        price = products[name]["price"]
        subtotal = price * quantity

        cart_items.append({
            "name": name,
            "price": price,
            "quantity": quantity,
            "subtotal": subtotal,
            "icon": products[name]["icon"]
        })

    cart_total = get_cart_total()
    cart_count = get_cart_count()

    # Order history
    connection = sqlite3.connect("shopcart.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, customer_name, email, mobile,
               address, payment_method, total_amount
        FROM orders
        ORDER BY id DESC
    """)

    orders = cursor.fetchall()

    connection.close()

    return render_template(
        "index.html",
        products=products,
        cart_items=cart_items,
        cart_total=cart_total,
        cart_count=cart_count,
        orders=orders
    )


# =========================
# ADD TO CART
# =========================
@app.route("/add/<name>")
def add_to_cart(name):

    if name in products:

        if name in cart:
            cart[name] += 1
        else:
            cart[name] = 1

    return redirect(url_for("home"))


# =========================
# INCREASE QUANTITY
# =========================
@app.route("/increase/<name>")
def increase(name):

    if name in cart:
        cart[name] += 1

    return redirect(url_for("home"))


# =========================
# DECREASE QUANTITY
# =========================
@app.route("/decrease/<name>")
def decrease(name):

    if name in cart:

        cart[name] -= 1

        if cart[name] <= 0:
            del cart[name]

    return redirect(url_for("home"))


# =========================
# REMOVE PRODUCT
# =========================
@app.route("/remove/<name>")
def remove(name):

    if name in cart:
        del cart[name]

    return redirect(url_for("home"))


# =========================
# CLEAR CART
# =========================
@app.route("/clear-cart")
def clear_cart():

    cart.clear()

    return redirect(url_for("home"))


# =========================
# CHECKOUT
# =========================
@app.route("/checkout", methods=["GET", "POST"])
def checkout():

    if request.method == "POST":

        customer_name = request.form.get("customer_name")
        email = request.form.get("email")
        mobile = request.form.get("mobile")
        address = request.form.get("address")
        payment_method = request.form.get("payment_method")

        total_amount = get_cart_total()

        # Save order in database
        connection = sqlite3.connect("shopcart.db")
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO orders
            (
                customer_name,
                email,
                mobile,
                address,
                payment_method,
                total_amount
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            customer_name,
            email,
            mobile,
            address,
            payment_method,
            total_amount
        ))

        order_id = cursor.lastrowid

        connection.commit()
        connection.close()

        # Clear cart after order
        cart.clear()

        return render_template(
            "index.html",
            products=products,
            cart_items=[],
            cart_total=0,
            cart_count=0,
            orders=[],
            success=True,
            order_id=order_id,
            customer_name=customer_name,
            total_amount=total_amount
        )

    return redirect(url_for("home"))


# =========================
# ORDER HISTORY
# =========================
@app.route("/orders")
def orders():

    connection = sqlite3.connect("shopcart.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, customer_name, email, mobile,
               address, payment_method, total_amount
        FROM orders
        ORDER BY id DESC
    """)

    order_list = cursor.fetchall()

    connection.close()

    return render_template(
        "index.html",
        products=products,
        cart_items=[],
        cart_total=0,
        cart_count=0,
        orders=order_list
    )


# =========================
# START APPLICATION
# =========================
if __name__ == "__main__":

    create_database()

    app.run(debug=True)