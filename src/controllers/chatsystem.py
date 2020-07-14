from pymongo import MongoClient
from src.config import *
from flask import request
from flask import Flask
from src.app import app
from bson.json_util import dumps

client = MongoClient(DBURL)
db = client.get_database()

#User Endpoints
@app.route("/user/create/<username>")
def createUser(username):
    new_user = {"name":username}
    check_user = db.user.distinct(username)
    if username in check_user:
        raise ValueError ("This username already exists. Please, try with other name")
    else:
        add_user = db.user.insert_one(username)
        print("VHJVJKH;VKJ;HMBKJH;",username)
        return dumps(f"New user created. Name: {username} and user_id: {add_user.inserted_id}")

"""
#Sentence Endpoints
@app.route("sentence/create/<text>")
def createSentence(text):
"""