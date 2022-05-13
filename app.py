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

# converter:variable_name

@app.route('/details/<a_country>', methods=['GET'])
def details(a_country):
    details_str= get_details(a_country)
    return details_str


app.run()