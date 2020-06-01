#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 29 13:29:10 2020

@author: arminhadzalic
"""

from flask import Flask
from flask import request
from flask import make_response
from flask import abort
from flask import render_template

from jsonutilities import jsonutils 
import logutilities

# Define the logger and the entry string (here "server") within the log file
logging = logutilities.logger.setLoggerName("server")


app = Flask(__name__)

@app.route('/', methods=['GET'])
def show_form():
    #make sure a templates folder and a index.html inside exist! 
        return render_template("index.html")
    
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == "POST":
        logging.info("request method is POST")
    if request.is_json:
        logging.info("received json")
        
        logging.info("get content...")
        jsoncontent = request.get_json()
        
        logging.info("check json format...")

        json = jsonutils()
        json.checkRequest(jsoncontent)
        
        prediction_result = do_predict(jsoncontent)
        
        response = make_response(prediction_result)
        response.mimetype = 'application/json'
        logging.info("responding result to client...")
        return response
    else:
        #logger.info("invalid json received")
        abort("invalid json", 400)


@app.errorhandler(404)
def not_found(error):
    return make_response({'error': 'Not found'}, 404)


def do_predict(text):
    # simple query about the length of the json file (len(text)) 
    # more complex methods/ calls are possible of course
    if len(text) % 2 == 0:
        logging.info("even")
        print("result is: even")
        return {"1st predicted name":"X"}
    else:
        logging.info("odd")
        print("result is: odd")
        return {"2nd predicted name":"Y"}

# Main
if __name__=='__main__':
    app.run() 
    
    
    
    
    