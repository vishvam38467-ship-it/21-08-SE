names = ['Shoes', 'Bag', 'Watch', 'Headphones']
prices = [999, 1500, 700, 2200]
expensive_products = [(names[i], prices[i]) for i in range(len(names)) if prices[i] > 1000]
print("pro3 - Products above 1000:", expensive_products)