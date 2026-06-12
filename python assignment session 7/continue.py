messages = ['Hi', 'Spam', 'Hello', 'Spam', 'How are you?']

for msg in messages:
    if msg == 'Spam':
        continue  # skip spam messages
    if msg == 'How are you?':
        break  # stop reading further
    print(msg)