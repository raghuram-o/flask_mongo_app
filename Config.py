from flask import Flask
from flask_mongoengine import MongoEngine
#from py_eureka_client import eureka_client

# make sure to add necessary code to configure you app with eureka server.
app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'host':"mongodb://localhost:27017/FrescoTweet"}
db=MongoEngine(app)

#eureka_server_url = "http://localhost:8761"
#eureka_client.init(eureka_server=eureka_server_url,app_name="DBRESTAPI", instance_port=5000)
