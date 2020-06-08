#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 29 13:27:43 2020

@author: arminhadzalic
"""

import requests
import sys

# Define URL of the application / webserver
predict = 'http://127.0.0.1:5000/predict'

class client:
    def __init__(self, args):
        #self.args = sys.argv
        client.main(self, args)
       

    def sendPayload(self,text):
        # prepare sample payload string
        # payload = '''{
        #    "title" : "Some title for a BugRequest",
        #    "description" : "The description for the bug",
        #    "component" : "Component affected by the bug"
        #}'''
        payload = text
        log.info("\nNew request sequence started #################################")
        log.info("prepared payload is: \n%s" %payload)


        try:
            log.info("try sending the request...")
            r = requests.post(predict, json=payload)
        except Exception as e:
            log.error("sending request failed:", exc_info=True)

        log.info("receiving result...")
        result = r.json()
        log.info("result is: %s" %result)

        #r.url
        #r.text
        #r.encoding
        #r.json()
        #r.raise_for_status()
        #r.status_code
        #r.raw


    def checkAndGetParams(self,argList):
        if len(argList) >= 2:
            print("Argument is: %s" %str(argList[1]))
            argument = str(argList[1])
            return argument
        else:
            print("Invalid arguments! Closing application...")
            sys.exit()


    def defineLogging(self):
        # Define the logger and the entry string (here "Client") within the log file
        import sys
        sys.path.insert(0, '../../logging/')
        from logutilities import logger
        log = logger.getLogger("Client")
        return log


    def main(self,args):
        global log 
        log = client.defineLogging(self)
        text = client.checkAndGetParams(self,args)
        client.sendPayload(self,text)


if __name__ == "__main__":
    cl = client(sys.argv)
