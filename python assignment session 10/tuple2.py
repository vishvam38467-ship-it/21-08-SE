fav_apps = ('Instagram', 'Zomato', 'Spotify', 'WhatsApp', 'Notion')
print("Original tuple:", fav_apps)
fav_apps[0]='youtube'
"""
Why this happens:
Tuples are immutable in Python. Once a tuple is created, you cannot modify, add, or
remove its elements. Any attempt to assign a new value to an existing index like
fav_apps[0] = 'YouTube' raises a TypeError.
"""