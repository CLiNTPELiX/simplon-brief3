import json
import pymongo
from flask import Flask, request, render_template


app = Flask(__name__)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["myrssdb"]
mycol = mydb["myrsscol"]

@app.route('/getall/')
def get():
    documents = mycol.find()
    res = []
    for document in documents:
        document['_id'] = str(document['_id'])
        res.append(document)
    return json.dumps(res)

@app.route('/search/', methods= ['GET', 'POST'])
def query():
    request.method=='POST'
    res = request.form.get('query')
    mycoll = mycol.find( {'query':res} )
    print(res)
    return render_template('index.html', data=mycoll) 
    