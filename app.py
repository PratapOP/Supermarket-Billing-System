from flask import request, redirect, url_for, session, render_template
from services.cart_logic import add_to_cart, remove_from_cart
from services.billing_logic import calculate_bill
from flask import Flask
app = Flask(__name__)

app.secret_key = "phase2-secret"


PRODUCTS = {
    1: {"id": 1, "name": "Amul Milk 1L", "price": 60, "gst": 5},
    2: {"id": 2, "name": "Basmati Rice 5kg", "price": 520, "gst": 5},
    3: {"id": 3, "name": "Sugar 1kg", "price": 45, "gst": 5},
    4: {"id": 4, "name": "Fortune Oil 1L", "price": 180, "gst": 5},
    5: {"id": 5, "name": "Brown Bread", "price": 40, "gst": 5},
    6: {"id": 6, "name": "Eggs (12 Pack)", "price": 70, "gst": 0},
}

@app.route("/add-to-cart/<int:product_id>")
def add_item(product_id):
    product = PRODUCTS.get(product_id)
    if not product:
        return "Product not found", 404

    cart = session.get("cart", {})
    cart = add_to_cart(cart, product)
    session["cart"] = cart

    return redirect(url_for("cart"))
@app.route("/cart")
def cart():
    cart = session.get("cart", {})
    bill = calculate_bill(cart)
    return render_template("cart.html", cart=cart, bill=bill)

@app.route("/add-demo-item")
def add_demo_item():
    product = {
        "id": 1,
        "name": "Amul Milk 1L",
        "price": 60,
        "gst": 5
    }

    cart = session.get("cart", {})
    cart = add_to_cart(cart, product)
    session["cart"] = cart

    return "Item added to cart"
@app.route("/remove/<int:product_id>")
def remove_item(product_id):
    cart = session.get("cart", {})
    cart = remove_from_cart(cart, product_id)
    session["cart"] = cart
    return redirect(url_for("cart"))


@app.route("/bill-demo")
def bill_demo():
    cart = session.get("cart", {})
    bill = calculate_bill(cart)
    return bill

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/checkout")
def checkout():
    cart = session.get("cart", {})
    bill = calculate_bill(cart)
    return render_template("checkout.html", bill=bill)

@app.route("/invoice")
def invoice():
    cart = session.get("cart", {})
    bill = calculate_bill(cart)
    return render_template("invoice.html", cart=cart, bill=bill)

@app.route("/customer/analytics")
def customer_analytics():
    return render_template("customer/analytics.html")

@app.route("/cashier/billing")
def cashier_billing():
    return render_template("cashier/billing.html")

@app.route("/admin/dashboard")
def admin_dashboard():
    return render_template("admin/dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)
