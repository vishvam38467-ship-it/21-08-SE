def display_friends(friends_dict):
    for username, followers in friends_dict.items():
        # Convert to K format if >= 1000
        if followers >= 1000:
            formatted = f"{followers/1000:.1f}K"
        else:
            formatted = str(followers)
        print(f"{username}: {formatted} followers")
        print("\npro3 - Friends list:")
instagram_friends = {
    'travel_ahmedabad': 15400,
    'foodie_diaries': 2300,
    'code_with_me': 890
}
display_friends(instagram_friends)