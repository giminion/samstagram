from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from bson import json_util
app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb+srv://loki:0000@cluster0.wcufqip.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/jwpage')
def gotojwpage():
    return render_template('jwpage.html')

@app.route('/mhpage')
def gotomhpage():
    return render_template('mhpage.html')

@app.route('/dspage')
def gotodspage():
    return render_template('dasol.html')

#내 파이몽고
@app.route("/guestbook", methods=["POST"])
def guestbook_post():
    insta_comment_receive = request.form['insta_comment_give']
    doc = {
        'insta_comment': insta_comment_receive
    }
    db.insta_main.insert_one(doc)
    return jsonify({'msg': '저장 완료!'})

@app.route("/guestbook", methods=["GET"])
def guestbook_get():
    comment= list(db.insta_main.find({},{'_id':False}))
    return jsonify({'result': comment})

#민현님 파이몽고
@app.route('/mhbook', methods=['POST'])
def mhbook_post():
   name_receive = request.form['name_give']
   doc = {
        'name': name_receive
    }
   db.namelist.insert_one(doc)
   return jsonify({'msg': '저장 완료!'})

@app.route('/mhbook', methods=['GET'])
def mhbook_get():
   name= list(db.namelist.find({},{'_id':False}))
   return jsonify({'result': name})

#다솔님 파이몽고
@app.route("/dsbook", methods=["POST"])
def dsbook_post():
    insta_comment_receive2 = request.form['insta_comment_give2']
    doc = {
        'comment2': insta_comment_receive2
    }
    db.ds.insert_one(doc)
    return jsonify({'msg': '저장 완료!'})

@app.route("/dsbook", methods=["GET"])
def dsbook_get():
    comment2= list(db.ds.find({},{'_id':False}))
    return jsonify({'result2': comment2})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)