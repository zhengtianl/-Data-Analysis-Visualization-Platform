"""test Flask with this"""
import couchdb
from flask import Flask, render_template
app = Flask(__name__)

# connect to the local CouchDB instance
couch = couchdb.Server()

# get a reference to an existing database
db = couch['mydatabase']


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/sentiment')
def sentiment():
    return 'sentiment'


@app.route("/map")
def map_render():
    return render_template("src/FrontEnd/public/index.html")