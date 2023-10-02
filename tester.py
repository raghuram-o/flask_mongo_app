import string, random
import json
from flask import jsonify
try:
    import pymongo, json, requests,mongoengine
    from bson.json_util import dumps
except:
    pass

FS_SCORE = 10
myclient = ""
try:
    myclient=mongoengine.connect(host='mongodb://localhost:27017/FrescoTweet')
    userPosts=myclient.FrescoTweet.userPosts
#    print("mongodb", userPosts)
except:
    pass


def randomString(stringLength=20):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


POST_BODY = randomString()

#try:
#    url = 'http://localhost:8761'
#    x = requests.get(url)
#    if 'DBRESTAPI' in x.text:
#        FS_SCORE += 10
#except:
#    pass

try:
    userPosts.delete_many({})
except:
    print("delete exception")
    pass

url = 'http://localhost:5000/addpost'
myobj = {"userId": "user@gmail.com", "postBody": POST_BODY}
headers = {'Content-Type': 'application/json'}

try:
    myData = json.dumps(myobj)
    x = requests.post(url, headers=headers, data=myData)
    mycl =(userPosts.find({}))
        # Checking Status
    for data in mycl:
        if x.status_code == 201:
            FS_SCORE += 5
        if len(data) > 0:
            if data['_id'] == 'user@gmail.com':
                FS_SCORE += 5
            data = data['posts']
            if len(data) > 0:
                data = data[0]
                if data['postBody'] == POST_BODY:
                    FS_SCORE += 5
                if data['postDate'] != None or data['postDate'] != "":
                    FS_SCORE += 5
except Exception as e:
    print("addpost exception")
    pass

print("after addpost, need_score = 30")
print("got_score = ",FS_SCORE)

url = 'http://localhost:5000/getpost/user@gmail.com'
try:
    x = requests.get(url)
    if x.status_code == 200:
        data = x.json()
        if len(data) > 0:
            data = data[0]
            if (data['postBody']):
                data['postBody']= POST_BODY
                FS_SCORE += 20
except:
    pass

print("after getpost, need_score = 50")
print("got_score = ",FS_SCORE)

try:
    url = 'http://localhost:5000/delpost/unknown@gmail.com'
    myobj = {'postId': data['postId']}
    x = requests.delete(url, headers=headers, data=json.dumps(myobj))
    if x.status_code == 404:
        FS_SCORE += 2

    url = 'http://localhost:5000/delpost/user@gmail.com'
    myobj = {'postId': data['postId']}
    myData = json.dumps(myobj)
    x = requests.delete(url, headers=headers, data=myData)
    if x.status_code == 200:
        FS_SCORE += 3
    mycls =userPosts.find({})
    if len(mycls[0]['posts']) == 0:
        FS_SCORE += 15
except Exception as e:
    print("delete caught exception", e)
    pass

print("after delpost, unknow (2), and delpost user(18), need_score = 70")
print("got_score = ",FS_SCORE)

try:
    userPosts.delete_many({})

    url = "http://localhost:5000/addpost"
    myData = json.dumps({"userId": "user@gmail.com", "postBody": "the count is more, when you reach the heights"})
    x = requests.post(url, headers=headers, data=myData)

except:
    pass

try:
    url = 'http://localhost:5000/searchpost/unknown@gmail.com'
    myobj = {'searchText': 'unknownWord'}
    myData = json.dumps(myobj)
    x = requests.options(url)
    y = requests.post(url, headers=headers, data=json.dumps(myobj))
    if 'Allow' in x.headers and y.status_code == 404:
        FS_SCORE += 2
    url = 'http://localhost:5000/searchpost/user@gmail.com'
    myobj = {'searchText': 'count'}
    myData = json.dumps(myobj)
    x = requests.post(url, headers=headers, data=myData)
    if x.status_code == 200:
        FS_SCORE += 3
        data = x.json()
    
        if len(data) > 0:
            data = data[0]
        
            if data['postBody'] == "the count is more, when you reach the heights":
                FS_SCORE += 10
except Exception as e:
    pass

print("after search post Allow(2), status200(3), found(10), need_score = 85")
print("got_score = ",FS_SCORE)

try:
    url = 'http://localhost:5000/subscribe/unknown@gmail.com'
    myobj = {'subscriber': 'user2@gmail.com'}
    x = requests.options(url)
    y = requests.post(url, headers=headers, data=json.dumps(myobj))
    if 'Allow' in x.headers and y.status_code == 404:
        FS_SCORE += 2


    url = 'http://localhost:5000/subscribe/user@gmail.com'
    myobj = {'subscriber': 'user2@gmail.com'}
    x = requests.post(url, headers=headers, data=json.dumps(myobj))
    if x.status_code == 200:
        FS_SCORE += 3
        data = x.json()
        print(data)
        if data['subscribed'][0] == "user2@gmail.com":
            FS_SCORE += 10
except:
    pass

print("after subscribed, allow(2), status200(3), found(10), need_score = 100")
print("got_score = ",FS_SCORE)

print("FS_SCORE:" + str(FS_SCORE) + "%")
