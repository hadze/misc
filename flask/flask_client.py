#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 29 13:27:43 2020

@author: arminhadzalic
"""

import requests
import logutilities

# Define URL of the application / webserver
url = 'http://127.0.0.1:5000'
predict = 'http://127.0.0.1:5000/predict'

# Define the logger and the entry string within the log file
logging = logutilities.logger.setLoggerName("client")

# prepare sample payload string
payload = '''{
    "title" : "Some title for a BugRequest",
    "description" : "The description for the bug",
    "component" : "Component affected by the bug"
}'''
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

#print(r.url)
#print(r.text)
#r.encoding
#r.json()
#r.raise_for_status()
#r.status_code
#r.raw

# Create file with the result
with open("jsonresult", 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)