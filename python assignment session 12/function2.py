def format_follower_count(number):
    if number >= 1000000:
        return f"{number / 1000000:.1f}M"
    elif number >= 1000:
        return f"{number / 1000:.1f}K"
    else:
        return str(number)

print("pro2 - Format examples:")
print("1500 ->", format_follower_count(1500))
print("1200000 ->", format_follower_count(1200000))
print("850 ->", format_follower_count(850))