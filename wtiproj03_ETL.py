import pandas as pd
import dataframe as df
import json
import time

class Tools:

    def __init__(self):
        self.__users_ratings_indexed = pd.DataFrame()
        self.__movie_genres = pd.read_csv('/home/peter/Studia/WTI/movie_genres.dat', sep='\t', dtype={"movieID": int})
        self.__rated_movies = pd.read_csv('/home/peter/Studia/WTI/user_ratedmovies.dat', sep='\t', dtype={"movieID": int})

        movie_genres_dummy = self.__movie_genres.copy()
        movie_genres_dummy['dummy_column'] = 1

        pivoted = movie_genres_dummy.pivot_table(index=['movieID'],
                                                 columns='genre',
                                                 values='dummy_column',
                                                 fill_value=0).add_prefix("genre-")

        self.__movie_genres_names=pivoted.columns

        self.__joined = pd.merge(self.__rated_movies, pivoted, on="movieID") \
                   .drop(["date_day", "date_minute", "date_month",
                         "date_second", "date_year", "date_hour"], axis=1).astype(int)


    def get_users_ratings(self):
        return self.__users_ratings


    def get_movie_genres_names(self):
        return self.__movie_genres_names


    def get_ratings_per_movie_per_user(self):
        for index, row in self.__joined.iterrows():
            yield row.to_json()

    def get_ratings_per_movie_per_user_dict(self):
        for index, row in self.__joined.iterrows():
            yield row.to_dict()

if __name__ == '__main__':
    tools=Tools()
    for elo in tools.get_ratings_per_movie_per_user():
        print(elo)