#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 29 13:29:10 2020

@author: arminhadzalic
"""

from flask import Flask, request, make_response, abort, render_template
from jsonutilities import jsonutils 

app = Flask(__name__)

@app.route('/', methods=['GET'])
def show_form():
    #make sure a templates folder and a index.html inside exist! 
        return render_template("index.html")
    
@app.route('/predict', methods=['POST'])
def predict():
    if request.is_json:
        log.info("received json")
        
        log.info("get content...")
        jsoncontent = request.get_json()
        log.info(jsoncontent)

        log.info("check json format...")
        json = jsonutils()
        reqOk = json.checkRequest(jsoncontent)

        if reqOk:
            prediction_result = do_predict(jsoncontent)
            response = make_response(prediction_result)
            response.mimetype = 'application/json'
            log.info("responding result to client...")
            return response
        else:
            log.error("check json format failed!")
            return "error in prediction!"
    else:
        log.error("invalid json")
        abort("invalid json", 400)


@app.errorhandler(404)
def not_found(error):
    return make_response({'error': 'Not found'}, 404)


def do_predict(text):
    # simple query about the length of the json file (len(text)) 
    # more complex methods/ calls are possible of course
    if len(text) % 2 == 0:
        log.info("even")
        print("result is: %s" %text)
        return text
    else:
        log.info("odd")
        print("result is: %s" %text)
        return text


def defineLogging():
    # Define the logger and the entry string (here "Server") within the log file
    import sys
    sys.path.insert(0, '../../logging/')
    from logutilities import logger
    log = logger.getLogger("Server")
    return log


# Main
if __name__=='__main__':
    log = defineLogging()
    app.run() 
    