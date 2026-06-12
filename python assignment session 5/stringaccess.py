"""
Given the string user_bio = 'Music lover | Foodie | Traveller', use a for loop to count and print the number of characters (excluding spaces) in the bio.
Hint:Use an if statement inside the loop to skip spaces.
"""
string_user_bio = 'music lover'
char_count = 0
for char in string_user_bio:
    if char != '':
        char_count+=1
print("number of charecters excluding the spaces ",char_count)