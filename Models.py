from mongoengine import *
from Config import db
from datetime import datetime


class Post(db.EmbeddedDocument):
    postId = SequenceField()
    postBody = StringField()
    postDate = StringField(default=datetime.utcnow().strftime("%d/%m/%Y"))

class userPosts(db.Document):
    userId = StringField(primary_key=True)
    posts = ListField(EmbeddedDocumentField(Post))
    subscribed = ListField()

    meta = {'collection': 'userPosts'}

