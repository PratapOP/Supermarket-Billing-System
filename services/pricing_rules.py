def get_gst_rate(category):
    gst_rates = {
        "grocery": 5,
        "dairy": 5,
        "essential": 0
    }
    return gst_rates.get(category, 5)
