from flask import Flask, render_template, jsonify
import requests
from pymongo import MongoClient
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
client = MongoClient()
records = client['fraud']['records']

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

@app.route('/getall')
def getall():
    o = []
    rs = records.find().sort([('_id', 1)]).limit(3)
    for r in rs:
        j = {}
        j['venue'] = r['venue_name']
        j['prediction'] = r['prediction']
        o.append(j)
    return jsonify(o)

if __name__ == "__main__":
    print 'a'
    app.run(host='0.0.0.0', port=3333, debug = True)





    # def prediction(json):
    #     prediction = mongo.db.users.find_one_or_404(json)
