from bson.json_util import dumps
from flask_restx import reqparse
from flask import jsonify, request,Response
from flask_cors import CORS, cross_origin
from Config import app,db
from Models import *
import json
from datetime import datetime
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

#            This routes are responsible for the REST operations
#            Make sure to add required decorators and complete the functions


def add_post():
    body = request.get_json()
    post_obj = Post(postBody = body.get("postBody"))
    userposts_obj = userPosts()
    userposts_obj.userId = body.get("userId")
    userposts_obj.posts = [post_obj]
    userposts_obj.save()
    return jsonify(userposts_obj), 201

def get_posts(userId):
    userposts_obj = userPosts.objects.get_or_404(userId=userId)
    return jsonify(userposts_obj.posts), 200


def del_posts(userId):
    userposts_obj = userPosts.objects.get_or_404(userId=userId)
    userposts_obj.update(posts=[])
#    userposts_obj.save()
    return jsonify(userposts_obj), 200
    
