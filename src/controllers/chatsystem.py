from pymongo import MongoClient
from src.config import *
from flask import request
from flask import Flask
from src.app import app
from bson.json_util import dumps

client = MongoClient(DBURL)
db = client.get_database()

@app.route("/")
def first_page():
    return 'Hello, user! Welcome to my Messenger API.'

# 1 User Endpoints
@app.route("/user/create/<username>")
def createUser(username):
    new_user = {"name":username}
    print(new_user)
    check_user = db.users.distinct("name")
    if username in check_user:
        return dumps("User already exists. Please, try with other name")
    else:
        db.users.insert_one(new_user)
        return dumps(f"New user created. Name: {username}")



#2 Chat Endpoints
@app.route("/chat/create/<chatname>")
def newChat(chatname):
    chats = db.conversations.distinct("chat_name")
    if chatname in chats:
        return dumps("Chat already exists. Please, try with another chat name")
    else:
        infochat = {"chat_name":chatname}
        db.conversations.insert_one(infochat)
        res = db.conversations.find_one({"chat_name":chatname},{"_id":1,"chat_name":1})
        return dumps(res)


@app.route("/chat/<chatname>/adduser/<user>")
def addUser(chatname,user):
    print(user)
    chat_id = db.conversations.find_one({"chat_name":chatname},{"_id":1})
    print(chat_id)
    if len(chat_id)==0:
        return dumps("Chat doesn't exist. Please try again")
    else:
        user_id = db.users.find_one({"name":user},{"_id":1})
        print(user_id)
        db.conversations.update({ "_id":chat_id["_id"]},{ "$push":{ "participants":user_id["_id"]}})
        res = db.conversations.find_one({"chat_name":chatname},{"participants":1})
        users = [db.users.find_one({"_id":part},{"_id":0,"name":1})["name"] for part in res["participants"]]
        dic = {"chat_name":chatname,"participants":users}
        return dumps(dic)
   


@app.route("/chat/<chatname>/user/<username>/addmessage/<message>")
def newMessage(chatname,username,message):
    chat_id = db.conversations.find_one({"chat_name":chatname},{"_id":1})
    print(chat_id)
    if len(chat_id)==0:
        return dumps("Chat doesn't exist. Please try again")
    user_id = db.users.find_one({"name":username},{"_id":1})
    print(user_id)
    if user_id==0:
        raise APIError ("Username doesn't exist, please check your spelling")
    else:
        message_info={"user":user_id["_id"],"name":username, "chat":chat_id["_id"],"chat_name": chatname, "message":message}
        db.chatproject.insert_one(message_info)
        res=db.chatproject.find_one({"message":message},{"_id":0})
        dic={"chat_name":chatname,"name":username,"message":res["message"]}
        return dumps(dic)


@app.route("/chat/<chatname>/list")
def getMessages(chatname):
    res = db.chatproject.find({"chat_name":chatname},{"chat_name":1,"message":1})
    lista = list(res)
    a = [lista[i]["message"] for i in range(len(lista))]
    dic = {"chat_name":chatname,"message":a}
    return dumps(dic)
