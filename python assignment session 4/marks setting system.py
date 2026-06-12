#Build a Python script that asks the user for their marks (0-100) and prints their grade based on this rule: 90+ = 'A', 75-89 = 'B', 60-74 = 'C', 40-59 = 'D', below 40 = 'F'. Use if, elif, and else.
a = int(input("enter your marks"))
if a >=90:
    print("A")
elif a >=75 and a <=89:
    print("B")
elif a >=60 and a <=74:
    print("C")
elif a >=40 and a <=59:
    print("D")
else:
    print("f")
    
