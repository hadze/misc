#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 29 13:27:43 2020

@author: arminhadzalic
"""

import requests
import logutilities
import sys

# Define URL of the application / webserver
predict = 'http://127.0.0.1:5000/predict'

# Define the logger and the entry string (here "client") within the log file
logging = logutilities.logger.setLoggerName("client")


def sendPayload(text):
    # prepare sample payload string
    # payload = '''{
    #    "title" : "Some title for a BugRequest",
    #    "description" : "The description for the bug",
    #    "component" : "Component affected by the bug"
    #}'''
    payload = text
    logging.info("\nNew request sequence started #################################")
    logging.info("prepared payload is: \n%s" %payload)


    try:
        logging.info("try sending the request...")
        r = requests.post(predict, json=payload)
    except Exception as e:
        logging.error("sending request failed: %s" %e)

    logging.info("receiving result...")
    result = r.json()
    logging.info("result is: %s" %result)

    #r.url
    #r.text
    #r.encoding
    #r.json()
    #r.raise_for_status()
    #r.status_code
    #r.raw


def checkAndGetParams(argList):
    if len(argList) >= 2:
        print("Argument is: %s" %str(argList[1]))
        argument = str(argList[1])
        return argument
    else:
        print("Invalid arguments! Closing application...")
        sys.exit()


def main(params):
    text = checkAndGetParams(params)
    sendPayload(text)

if __name__ == "__main__":
    main(sys.argv)