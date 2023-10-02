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

def search_user(userId):
    body = request.get_json()
    userposts_obj = userPosts.objects.get_or_404(userId=userId)
    return jsonify(userposts_obj.posts), 200


def subscriber(userId):
    body = request.get_json()
    userposts_obj = userPosts.objects.get_or_404(userId=userId)
    if "subscriber" in body:
        subscription = userposts_obj.subscribed
        subscription.append(body.get("subscriber"))
        userposts_obj.update(subscribed=subscription)
    return jsonify(userposts_obj), 200
