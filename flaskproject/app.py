import re
import json
from flask import Flask
from datetime import datetime
from distutils.log import debug
from fileinput import filename
from flask import *  

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, Pythin!"

@app.route('/success', methods = ['GET'])  
def success():  
    if request.method == 'GET':  
        #f = request.files['file']
        #//f.save(f.filename)  
        return type("Done")  
  


@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content