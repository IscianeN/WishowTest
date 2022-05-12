import flask
from connection_to_db import *
from scraper import *
from countries_controller import *



app = flask.Flask(__name__)

app.config["DEBUG"] = True

    
@app.route('/', methods=['GET'])
def home():
    return "TEST"

@app.route('/countries', methods=['GET'])
def display():
    return countries_str

@app.route('/details/<country>', methods=['GET'])
def details(country):
    result = get_details_country()
    return result
    
app.run()