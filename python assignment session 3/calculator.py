print("1.addition")
print("2.subtraction")
print("3.division")
print("4.multiplication")
a = int(input("enter your choice from 1 to 4"))
if a == 1:
    a1 = int(input("enter your number 1"))
    a2 = int(input("enter your number 2"))
    c = a1+a2
    print(c)
elif a == 2:
    a1 = int(input("enter your number 1"))
    a2 = int(input("enter your number 2"))
    d = a1-a2
    print(d)
elif a ==3:
    a1 = int(input("enter your number 1"))
    a2 = int(input("enter your number 2"))
    e = a1/a2
    print(e)
elif a == 4:
    a1 = int(input("enter your number 1"))
    a2 = int(input("enter your number 2"))
    f = a1*a2
    print(f)
else:
    print("incorrect choice entered")