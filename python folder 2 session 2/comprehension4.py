ratings_matrix = [[4, 5, 3, 2], [5, 4, 4, 3], [3, 2, 5, 5]]
high_ratings = [rating for restaurant in ratings_matrix for rating in restaurant if rating > 4]
print("pro4 - Ratings above 4 flattened:", high_ratings)