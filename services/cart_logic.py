def add_to_cart(cart, product):
    product_id = str(product["id"])  # 🔥 FORCE STRING KEY

    if product_id in cart:
        cart[product_id]["quantity"] += 1
    else:
        cart[product_id] = {
            "name": product["name"],
            "price": product["price"],
            "gst": product["gst"],
            "quantity": 1
        }

    return cart

def remove_from_cart(cart, product_id):
    product_id = str(product_id)
    if product_id in cart:
        del cart[product_id]
    return cart

