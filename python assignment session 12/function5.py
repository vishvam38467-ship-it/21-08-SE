from functools import reduce

swiggy_prices = [120, 80, 150, 60]
total_bill = reduce(lambda x, y: x + y, swiggy_prices)
print("pro5 - Total Swiggy bill:", total_bill)