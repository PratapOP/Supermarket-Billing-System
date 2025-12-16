def calculate_bill(cart):
    subtotal = 0
    total_gst = 0

    for item in cart.values():
        item_total = item["price"] * item["quantity"]
        gst_amount = (item_total * item["gst"]) / 100

        subtotal += item_total
        total_gst += gst_amount

    discount = calculate_discount(subtotal)
    grand_total = subtotal + total_gst - discount

    return {
        "subtotal": subtotal,
        "gst": round(total_gst, 2),
        "discount": discount,
        "total": round(grand_total, 2)
    }


def calculate_discount(subtotal):
    if subtotal > 500:
        return 50
    return 0
