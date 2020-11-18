import os
import json
import pymongo
from flask import Flask, request, render_template

app = Flask(__name__)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["myrssdb"]
mycol = mydb["myrsscol"]

@app.route('/')
def get():
    documents = mycol.find()
    response = []
    for document in documents:
        document['_id'] = str(document['_id'])
        response.append(document)
    return json.dumps(response)

#def index():
    #for x in mycol.find({}):
    #    print(x)
    #return render_template('index.html')

@app.route('/greetings')
def greetings():
    return 'Je vous souhaite la bienvenue!'

@app.route('/display')
def info():        
    return 'Voici les infos'

@app.route('/contact')
def contact():
    return 'Page de contact'