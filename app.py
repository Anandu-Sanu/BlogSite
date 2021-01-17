from flask import Flask,request,jsonify
from flask_pymongo import PyMongo
from datetime import datetime

app =Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/blog"

mongo = PyMongo(app)

@app.route('/upload/post',methods=["POST"])
def create_article():
    # payload = request.json()

    result = mongo.db.articles.insert_one({
        "title":request.json["title"],
        "content":request.json["content"],
        "author":request.json["author"],
        "created_at":datetime.now()
    })
    return jsonify({"message":"Content Created Sucessfully",
                "content_id":result._id}),201

@app.route('/show/articles',methods=["GET"])
def show_article():
    payload = request.json()

    result = mongo.db.articles.find()
    return jsonify(result)


if __name__ == '__main__':
    app.run()