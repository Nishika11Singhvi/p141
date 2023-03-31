from flask import Flask, jsonify, request
import csv

all_movies=[]
with open("articles.csv", encoding="utf8") as f:
    reader=csv.reader(f)
    data=list(reader)
    all_movies=data[1:]

liked_articles=[]
notliked_articles=[]

app=Flask(__name__)
@app.route("/get-movie") 

def get_article():
    return jsonify({
        "data": all_articles[0],
        "status":"success"
    })

@app.route("/liked-article",methods=["POST"])

def liked_article():

    article=all_articles[0]
    all_articles=all_articles[1:]
    liked_articles.append(article) 

    return jsonify({
        "status":"success"
    })

@app.route("/notliked-article",methods=["POST"])

def notliked_article():

    article=all_articles[0]
    all_articles=all_articles[1:]
    notliked_articles.append(article) 

    return jsonify({
        "status":"success"
    })

if __name__=="__main__":
    app.run()

