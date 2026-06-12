user_word = input("enter the string")
word = ['a','e','i','o','u']
for char in user_word:
    for vowel in word:
        if char == vowel:
            print(char)