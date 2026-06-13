food_order = {'Pizza': 2, 'Burger': 1, 'Fries': 3}
print("\npro4 - Food order analysis:")
print("a) All food items:", list(food_order.keys()))
print("b) All quantities:", list(food_order.values()))
print("c) Each item with its quantity:")
for item, qty in food_order.items():
    print(f" {item}: {qty}")