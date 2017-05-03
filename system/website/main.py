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

@app.route("/presentation")
def presentation():
    return render_template('presentation.html')

@app.route('/getall')
def getall():
    o = []
    rs = records.find().sort([('_id', -1)]).limit(15)
    for r in rs:
        j = {}
        j['name'] = r['name']
        j['venue'] = r['venue_name']
        j['state'] = r['venue_state']
        j['prediction'] = r['prediction']
        j['probability'] = r['probability']
        o.append(j)
    return jsonify(o)

if __name__ == "__main__":
    print 'a'
    app.run(host='0.0.0.0', port=3333, debug = True)
