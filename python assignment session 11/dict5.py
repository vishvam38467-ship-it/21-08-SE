def update_cart(cart, item, qty):
    if item in cart:
        cart[item] += qty 
    else:
        cart[item] = qty 
    return cart

print("\npro5 - Cart updates:")
my_cart = {'Headphones': 1, 'Phone Case': 2}
print("Initial cart:", my_cart)

my_cart = update_cart(my_cart, 'Charger', 1) 
print("After adding Charger:", my_cart)

my_cart = update_cart(my_cart, 'Phone Case', 1) 
print("After updating Phone Case qty:", my_cart)