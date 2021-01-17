from flask import Flask,request,jsonify
import pymongo
from pymongo import MongoClient
import datetime

app =Flask(__name__)

# connection config to pymongo

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client['blogsite']
collection = db['posts']



@app.route('/upload/post',methods=["POST"])
def create_article():
    post = {    
                "author":request.json["author"],
                "title": request.json["title"],
                "content": request.json["content"],
                "date": datetime.datetime.utcnow()
            }
    posts=db.posts
    post_id=posts.insert_one(post).inserted_id
    return jsonify({"message":"Content Created Sucessfully",
                "content_id":result._id}),201

# @app.route('/show/articles',methods=["GET"])
# def show_article():
#     payload = request.json()

#     result = mongo.db.articles.find()
#     return jsonify(result)


if __name__ == '__main__':
    app.run()