from flask import Flask,jsonify,request
from flask_pymongo import PyMongo
from datetime import datetime

app =Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/blog"

mongo = PyMongo(app)

@app.route('/upload/post',METHOD=["POST"])
def create_article():
    payload = request.json()

    result = mongo.db.articles.insert_one({
        "title":payload.get("title"),
        "content":payload.get("content"),
        "author":payload.get("author"),
        "created_at":datetime.now()
    })
    return jsonify({"message":"Content Created Sucessfully",
                "content_id":result._id}),201

@app.route('/show/articles',METHOD=["GET"])
def show_article():
    payload = request.json()

    result = mongo.db.articles.find()
    return jsonify(result)


if __name__ == '__main__':
    app.run()