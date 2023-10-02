import PostsApi, Config, UserApi
from flask import jsonify
from Config import app

@app.route('/adder', methods=["GET"])
def rain():
    return jsonify("Success"), 200

@app.route('/addpost', methods=["POST"])
def addposting():
    return PostsApi.add_post()

@app.route('/getpost/<userId>', methods=["GET"])
def gettingposting(userId):
    return PostsApi.get_posts(userId)

@app.route('/delpost/<userId>', methods=["DELETE"])
def del_posting(userId):
    return PostsApi.del_posts(userId)

@app.route('/searchpost/<userId>', methods=["POST"])
def search_posting(userId):
    return UserApi.search_user(userId)

@app.route('/subscribe/<userId>', methods=["POST"])
def search_sub(userId):
    return UserApi.subscriber(userId)

if __name__ == '__main__':
    Config.app.run(debug=True, port=5000)
