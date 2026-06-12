"""
Write a Python program that takes your favorite cricket team's score as input and prints a message: if score is 200 or more, print 'High Score!', if between 150 and 199, print 'Good Score', if between 100 and 149, print 'Average', else print 'Needs Improvement'.
 Use if, elif, else.
"""
a = int(input("enter cricket team score"))
if a >=200:
    print("high score")
elif a <149:
    print("good score")
elif a <200:
    print("good score")
elif a<99:
    print("average")
elif a<148:
    print("average")
else:
    print("need improvement")