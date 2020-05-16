from wtiproj04.wtiproj04_ETL_and_data_processing import DataProcessing


def test_generate_avg_rating_per_genre():
    dp = DataProcessing()
    vector = dp.generate_avg_rating_per_genre()

    for x in vector.iterrows():
        key = x[0]  # key
        var = x[1]  # value
        x.


def test_get_ratings_per_genre_unbiased_data_frame():
    dp = DataProcessing()
    df_default = dp.get_joined()
    dp.get_vector_of_ratings_per_genre()
    df = dp.get_ratings_per_genre_unbiased_data_frame()

    for genre_name in dp.get_movie_genres_names():
        assert df_default[genre_name] != df[genre_name]
