#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 29 13:29:10 2020

@author: arminhadzalic
"""

from flask import Flask, request, make_response, abort, render_template

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
    if request.is_json:
        logging.info("received json")
        
        logging.info("get content...")
        jsoncontent = request.get_json()
        logging.info(jsoncontent)

        logging.info("check json format...")
        json = jsonutils()
        reqOk = json.checkRequest(jsoncontent)

        if reqOk:
            prediction_result = do_predict(jsoncontent)
            response = make_response(prediction_result)
            response.mimetype = 'application/json'
            logging.info("responding result to client...")
            return response
        else:
            logging.error("check json format failed!")
            return "error in prediction!"
    else:
        logging.error("invalid json")
        abort("invalid json", 400)


@app.errorhandler(404)
def not_found(error):
    return make_response({'error': 'Not found'}, 404)


def do_predict(text):
    # simple query about the length of the json file (len(text)) 
    # more complex methods/ calls are possible of course
    if len(text) % 2 == 0:
        logging.info("even")
        print("result is: %s" %text)
        return text
    else:
        logging.info("odd")
        print("result is: %s" %text)
        return text

# Main
if __name__=='__main__':
    app.run() 
    
    
    
    
    