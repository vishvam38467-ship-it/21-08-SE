a = input("enter the food item")
b = int(input("enter your quantity"))
if a == "pizza" and b <10:
    print("your entered quantity is",b)
    print(f"the cost is {b+15}.0 ")
elif a == "pasta" and b<=10:
    print("your entered quantity is",b)
    print(f"the cost is {b+10}")
else:
    print("error has been occured")