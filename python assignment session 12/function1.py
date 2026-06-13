# pro1: Define function get_discounted_price that takes price and discount_percent
def get_discounted_price(price, discount_percent):
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return final_price

print("pro1 - Price 500 with 10% discount:", get_discounted_price(500, 10))

