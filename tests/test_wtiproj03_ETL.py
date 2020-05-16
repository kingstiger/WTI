from wtiproj03.wtiproj03_ETL import Tools

exam_dict = [{'userID': 62394, 'movieID': 480, 'rating': 3, 'genre-Action': 1, 'genre-Adventure': 1,
              'genre-Animation': 0, 'genre-Children': 0, 'genre-Comedy': 0, 'genre-Crime': 0,
              'genre-Documentary': 0,
              'genre-Drama': 0, 'genre-Fantasy': 0, 'genre-Film-Noir': 0, 'genre-Horror': 0, 'genre-IMAX': 0,
              'genre-Musical': 0, 'genre-Mystery': 0, 'genre-Romance': 0, 'genre-Sci-Fi': 1, 'genre-Short': 0,
              'genre-Thriller': 1, 'genre-War': 0, 'genre-Western': 0},
             {'userID': 62394, 'movieID': 480, 'rating': 3, 'genre-Action': 1, 'genre-Adventure': 1,
              'genre-Animation': 0, 'genre-Children': 0, 'genre-Comedy': 0, 'genre-Crime': 0,
              'genre-Documentary': 0,
              'genre-Drama': 0, 'genre-Fantasy': 0, 'genre-Film-Noir': 0, 'genre-Horror': 0, 'genre-IMAX': 0,
              'genre-Musical': 0, 'genre-Mystery': 0, 'genre-Romance': 0, 'genre-Sci-Fi': 1, 'genre-Short': 0,
              'genre-Thriller': 1, 'genre-War': 0, 'genre-Western': 0}]


def test_add_ratings_from_dict():
    tools = Tools(empty=True)
    testing_list = []
    tools.add_ratings_from_dict(exam_dict)

    for x in tools.get_ratings_per_movie_per_user_dict():
        print(x)
        testing_list.append(x)

    assert len(testing_list) > 0

    for x in exam_dict:
        assert testing_list.__contains__(x)


def test_get_ratings_per_movie_per_user():
    tools = Tools()
    gen = tools.get_ratings_per_movie_per_user()
    testing_result = next(gen, 'EMPTY')

    assert testing_result != 'EMPTY'
    for x in exam_dict[1].keys():
        assert x in testing_result.__str__()
