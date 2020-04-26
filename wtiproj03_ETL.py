import pandas as pd
import dataframe as df
import json
import time


class Tools:

    # Zad 1
    def __init__(self):
        self.__users_ratings = None
        self.__users_ratings_indexed = pd.DataFrame()
        self.__movie_genres = \
            pd.read_csv('/home/peter/Studia/WTI/movie_genres.dat',
                        sep='\t',
                        dtype={"movieID": int})
        self.__rated_movies = \
            pd.read_csv('/home/peter/Studia/WTI/user_ratedmovies.dat',
                        sep='\t',
                        dtype={"movieID": int})

        movie_genres_dummy = self.__movie_genres.copy()
        movie_genres_dummy['dummy_column'] = 1

        pivoted = \
            movie_genres_dummy.pivot_table(index=['movieID'],
                                           columns='genre',
                                           values='dummy_column',
                                           fill_value=0).add_prefix("genre-")

        self.__movie_genres_names = pivoted.columns

        self.__joined = \
            pd.merge(self.__rated_movies, pivoted, on="movieID").drop(["date_day", "date_minute", "date_month",
                                                                       "date_second", "date_year", "date_hour"],
                                                                      axis=1).astype(int)

    def get_users_ratings(self):
        return self.__users_ratings

    def get_movie_genres_names(self):
        return self.__movie_genres_names

    # Zad 2
    def get_ratings_per_movie_per_user(self):
        for index, row in self.__joined.iterrows():
            yield row.to_json()

    def get_ratings_per_movie_per_user_dict(self):
        for index, row in self.__joined.iterrows():
            yield row.to_dict()


if __name__ == '__main__':
    tools = Tools()
    for something in tools.get_ratings_per_movie_per_user():
        print(something)

# Przykładowy wynik każdej iteracji w postaci JSON:
# {
#     "userID":1160,
#     "movieID":1240,
#     "rating":4,
#     "genre-Action":1,
#     "genre-Adventure":0,
#     "genre-Animation":0,
#     "genre-Children":0,
#     "genre-Comedy":0,
#     "genre-Crime":0,
#     "genre-Documentary":0,
#     "genre-Drama":0,
#     "genre-Fantasy":0,
#     "genre-Film-Noir":0,
#     "genre-Horror":0,
#     "genre-IMAX":0,
#     "genre-Musical":0,
#     "genre-Mystery":0,
#     "genre-Romance":0,
#     "genre-Sci-Fi":1,
#     "genre-Short":0,
#     "genre-Thriller":1,
#     "genre-War":0,
#     "genre-Western":0
# }
