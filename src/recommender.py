import pandas as pd

movies = pd.read_csv("data/tmdb_5000_movies.csv")
credits = pd.read_csv("data/tmdb_5000_credits.csv")

print("Movies Dataset:")
print(movies.head())

print("\nCredits Dataset:")
print(credits.head())

print("\nMovies Shape:", movies.shape)
print("Credits Shape:", credits.shape)