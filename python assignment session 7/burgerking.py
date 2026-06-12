foods = ['Pizza', 'Burger', 'Pasta', 'Sandwich', 'Burger King']

for item in foods:
    if item == 'Burger King':
        print('Found Burger King, stopping search.')
        break  # exit the loop entirely
    print(item)