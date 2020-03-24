from flask import Flask, jsonify, request, abort
import wtiproj03_ETL as Etl
import json

app=Flask(__name__)
app.config["DEBUG"]=True
tools = Etl.Tools()
rat = []
for i in range(0, 20):
    rat.append(next(tools.get_ratings_per_movie_per_user_dict()))

ratings = [
    {
        'id': 1,
        'title': u'genre-Anime',
        'rating': 420
    },
    {
        'id': 2,
        'title': u'genre-Porn',
        'rating': 69
    }
]
user_profiles = [
    {
        'user_id': 1,
        'genre-Action': 1,
        'genre-Adventure': 1,
        'genre-Animation': 1,
        'genre-Children': 1,
        'genre-Comedy': 1,
        'genre-Crime': 1,
        'genre-Documentary': 1,
        'genre-Drama': 1,
        'genre-Fantasy': 1,
        'genre-Film-Noir': 1,
        'genre-Horror': 1,
        'genre-IMAX': 1,
        'genre-Musical': 1,
        'genre-Mystery': 1,
        'genre-Romance': 1,
        'genre-Sci-Fi': 1,
        'genre-Short': 1,
        'genre-Thriller': 1,
        'genre-War': 1,
        'genre-Western': 1
    },
    {
        'user_id': 2,
        'genre-Action': 1,
        'genre-Adventure': 1,
        'genre-Animation': 1,
        'genre-Children': 1,
        'genre-Comedy': 1,
        'genre-Crime': 1,
        'genre-Documentary': 1,
        'genre-Drama': 1,
        'genre-Fantasy': 1,
        'genre-Film-Noir': 1,
        'genre-Horror': 1,
        'genre-IMAX': 1,
        'genre-Musical': 1,
        'genre-Mystery': 1,
        'genre-Romance': 1,
        'genre-Sci-Fi': 1,
        'genre-Short': 1,
        'genre-Thriller': 1,
        'genre-War': 1,
        'genre-Western': 1
    }
]

@app.route('/rating' , methods=['POST'])
def post_one_row():

    if not request.json:
        abort(400)
    if not 'movieID' in request.json:
        abort(400)

    content = request.get_json()
    rat.append(content)
    return content

@app.route('/ratings' , methods=['GET'])
def get_all_rows():
    return jsonify(rat)

@app.route('/ratings' , methods=['DELETE'])
def delete_rows():
    rat.clear()
    return ""

@app.route('/avg-genre-ratings/all-users' , methods=['GET'])
def read_all_ratings():
    return jsonify(user_profiles)

@app.route('/avg-genre-ratings/user' , methods=['GET'])
def read_ratings_of_user():
    if 'userID' in request.args:
        user_id = int(request.args['userID'])
    else:
        return "Error, no userID provided"

    for user in user_profiles:
        if int(user_id) == int(user['user_id']):
            return jsonify(user)
    return "Error, no such user"

app.run()

#save one row: POST on '/rating'
#read all rows: GET on '/ratings'
#delete all rows: DELETE on '/ratings'
#read all ratings of genres by all users: GET on '/avg-genre-ratings/all-users'
#read ratings of genres per user: GET on '/avg-genre-ratings/user<userID>'