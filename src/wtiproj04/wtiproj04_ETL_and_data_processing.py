from wtiproj03.wtiproj03_ETL import Tools
import pandas as pd
import numpy as np
from collections import defaultdict


class DataProcessing(Tools):

    def __init__(self):
        super().__init__()
        self.__ratings_per_movie_genre = pd.DataFrame()
        self.__ratings_per_genre_unbiased_data_frame = self.get_joined()
        self.__ratings_per_movie_genre_per_user = pd.DataFrame()
        self.__user_profile = pd.DataFrame()
        self.__avg_rating_per_movie_genre = {}
        self.generate_avg_rating_per_genre()

    def get_vector_of_ratings_per_genre(self):
        return self.__avg_rating_per_movie_genre

    def generate_avg_rating_per_genre(self):
        joined_dummy = pd.merge(self._rated_movies, self._movie_genres, on='movieID')
        pivoted = joined_dummy.pivot_table(columns='genre', fill_value=0, aggfunc=np.nanmean,
                                           values='rating').add_prefix('genre-')

        return pivoted

    def generate_avg_rating_per_genre_old(self):
        for row in self.get_ratings_per_movie_per_user_dict():
            for key in row:
                if key in self.__avg_rating_per_movie_genre:
                    self.__avg_rating_per_movie_genre[key].append(row["rating"])
                elif key != "movieID" and key != "userID" and key != "rating":
                    self.__avg_rating_per_movie_genre[key] = [row["rating"]]
        for genre in self.__avg_rating_per_movie_genre:
            self.__avg_rating_per_movie_genre[genre] = np.nanmean(self.__avg_rating_per_movie_genre[genre])

    def get_ratings_per_genre_unbiased_data_frame(self):
        self.__ratings_per_genre_unbiased_data_frame = self.get_joined()
        for col_name in self.get_movie_genres_names():
            self.__ratings_per_genre_unbiased_data_frame[col_name] = self.__ratings_per_genre_unbiased_data_frame[
                col_name].apply(lambda x: x - self.__avg_rating_per_movie_genre[col_name])
        return self.__ratings_per_genre_unbiased_data_frame


if __name__ == '__main__':
    dp = DataProcessing()
    df_default = dp.get_joined()
    dp.get_vector_of_ratings_per_genre()
    df = dp.get_ratings_per_genre_unbiased_data_frame()

    for k, v in df.iterrows():
        print(k)
        print("*")
        print(v)
        print("\n")
    for k, v in df_default.iterrows():
        print(k)
        print("*")
        print(v + "\n")
