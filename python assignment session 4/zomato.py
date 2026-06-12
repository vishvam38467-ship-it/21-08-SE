"""
Create a Python program that checks if a person can order food from Zomato late at night: input age and current time (24-hour format). 
If age is 18 or above and time is between 22 (10pm) and 2 (2am), print 'Order allowed', else print 'Order not allowed'.
Use nested if statements.
<br><br><em><strong>Hint:</strong> Handle the time range that crosses midnight by checking if time >= 22 or time <= 2.</em>
"""
a = int(input("enter your age"))
b = int(input("enter current time"))
if b>=22 or b<=2:
    if a>=18:
        print("order is allowed")
    else:
        print("order is not allowed")
