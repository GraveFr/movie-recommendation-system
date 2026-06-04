import pandas as pd
import ast

movies = pd.read_csv("data/tmdb_5000_movies.csv")
credits = pd.read_csv("data/tmdb_5000_credits.csv")

movies = movies.merge(credits, on="title")

movies = movies[[
    "movie_id",
    "title",
    "overview",
    "genres",
    "keywords",
    "cast",
    "crew"
]]

def convert(text):
    L = []
    for i in ast.literal_eval(text):
        L.append(i["name"])
    return L
def convert_cast(text):
    L = []
    counter = 0

    for i in ast.literal_eval(text):
        if counter != 3:
            L.append(i["name"])
            counter += 1
        else:
            break

    return L
def fetch_director(text):
    L = []

    for i in ast.literal_eval(text):
        if i["job"] == "Director":
            L.append(i["name"])
            break

    return L

movies["genres"] = movies["genres"].apply(convert)
movies["keywords"] = movies["keywords"].apply(convert)
movies["cast"] = movies["cast"].apply(convert_cast)
movies["crew"] = movies["crew"].apply(fetch_director)

print(movies[["title", "genres", "keywords", "cast", "crew"]].head())