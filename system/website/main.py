from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

if __name__ == "__main__":
    print 'a'
    app.run(host='0.0.0.0', port=3333, debug = True)





    # def prediction(json):
    #     prediction = mongo.db.users.find_one_or_404(json)
