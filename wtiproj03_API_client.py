import requests as req
import random
import json


class MyReq:

    def __init__(self, method, url, do_print=True, data=None):

        self.__url = url

        if data is not None:
            self.__response = method(url, json=data)
        else:
            self.__response = method(url)

        self.__status_code = self.__response.status_code
        self.__headers = self.__response.headers
        if method != req.delete:
            self.__content = self.__response.json()
        else:
            self.__content = ""

        if do_print:
            print('Method: ' + str(method).split()[1].swapcase() + ' at: ' + self.__url)
            print('Status code: ', self.__status_code)
            print("Headers: ", self.__headers)
            print('Content: ', self.__content)
            print("********************************")


def get_all_rows():
    print("********************************")
    print('get_all_rows')

    url = 'http://127.0.0.1:5000/ratings'
    MyReq(req.get, url)


def post_new_row():
    print("********************************")
    print('post_new_row')

    url = 'http://127.0.0.1:5000/rating'
    data = {
        "userID": random.randint(1, 99999),
        "movieID": random.randint(1, 999999),
        "rating": random.randint(0, 5),
        "genre-Action": random.randint(0, 5),
        "genre-Adventure": random.randint(0, 5),
        "genre-Animation": random.randint(0, 5),
        "genre-Children": random.randint(0, 5),
        "genre-Comedy": random.randint(0, 5),
        "genre-Crime": random.randint(0, 5),
        "genre-Documentary": random.randint(0, 5),
        "genre-Drama": random.randint(0, 5),
        "genre-Fantasy": random.randint(0, 5),
        "genre-Film-Noir": random.randint(0, 5),
        "genre-Horror": random.randint(0, 5),
        "genre-IMAX": random.randint(0, 5),
        "genre-Musical": random.randint(0, 5),
        "genre-Mystery": random.randint(0, 5),
        "genre-Romance": random.randint(0, 5),
        "genre-Sci-Fi": random.randint(0, 5),
        "genre-Short": random.randint(0, 5),
        "genre-Thriller": random.randint(0, 5),
        "genre-War": random.randint(0, 5),
        "genre-Western": random.randint(0, 5)
    }
    MyReq(req.post, url, data=json.dumps(data))


def read_user_ratings():
    print("********************************")
    print('read_user_ratings')

    url = 'http://127.0.0.1:5000/avg-genre-ratings/user?userID=1'
    MyReq(req.get, url)


def read_all_ratings():
    print("********************************")
    print('read_all_ratings')

    url = 'http://127.0.0.1:5000/avg-genre-ratings/all-users'
    MyReq(req.get, url)


def delete_all_rows():
    print("********************************")
    print('delete_all_rows')

    url = 'http://127.0.0.1:5000/ratings'
    MyReq(req.delete, url)


if __name__ == '__main__':
    methods = [get_all_rows, read_user_ratings, read_all_ratings, delete_all_rows, post_new_row, get_all_rows]
    controller = ""
    while 'N' not in controller and 'n' not in controller:
        for meh in methods:
            try:
                meh()
            except Exception as e:
                print(e)
        controller = input("Restart?")
