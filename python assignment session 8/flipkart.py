description = input("Enter Flipkart product description: ")
words = description.split() # split by spaces into a list

if words: # check if not empty
    first_word = words[0]
    last_word = words[-1]
    total_words = len(words)

    print(f"First word: {first_word}")
    print(f"Last word: {last_word}")
    print(f"Total words: {total_words}")
else:
    print("Empty description")