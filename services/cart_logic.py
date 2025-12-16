def add_to_cart(cart, product):
    if product["id"] in cart:
        cart[product["id"]]["quantity"] += 1
    else:
        cart[product["id"]] = {
            "name": product["name"],
            "price": product["price"],
            "gst": product["gst"],
            "quantity": 1
        }
    return cart


def remove_from_cart(cart, product_id):
    if product_id in cart:
        del cart[product_id]
    return cart
