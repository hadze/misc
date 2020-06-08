import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import json

import sys
sys.path.insert(0, '../flask/src/')

from flask_client import client

""" sys.path.insert(0, '../logging/')
import logutilities """

#show current working directory
#pwd

class EventHandler(FileSystemEventHandler):
    file_cache = {}

    def on_created(self, event):
        seconds = int(time.time())
        key = (seconds, event.src_path)
        print("Key: %s" %str(key))
        if key in self.file_cache:
            log.debug("already registered event")
            return
        self.file_cache[key] = True
        
        # Process the file
        file = event.src_path
        processFile(event, file)
    
    #def on_any_event (if everything should be traced)
    #...

def processFile(event, file):
    log.info("Trying to process file: %s" %file)
    try:
        with open(file, mode="r") as json_file:
            content = json_file.read()
            log.info("Opened json-file with this content: %s" %content)
            
    except ValueError as err:
        log.error("Error while reading file:", exc_info=True)
        return

    try:
        #load rawdata and create string with correctly formated JSON - with double quotes
        #{'a':1} --> {"a":1}
        rawdata = json.loads(content)
        data = json.dumps(rawdata)
    except ValueError as e:
        log.error("Invalid Json Format:", exc_info=True)
        return False
    
    log.info("sending data from filewatcher to client")
    data =[0, data]
    cl = client(data)
    #flask_client.sendPayload(data)

    print(event)

def checkAndGetDir(params):
    if len(sys.argv) >= 2:
        print("Path to be watched at is: %s" %str(sys.argv[1]))
        path = str(sys.argv[1])
        #TODO check if path is accessible
        return path
    else:
        print("Path not provided! Closing application...")
        sys.exit()


def observeDir(path):
    log.info("Watching at: %s ..." % path)
    print("Watching at: %s ..." % path)
    event_handler = EventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

def main(params):
    path = checkAndGetDir(params)
    observeDir(path)
        

def defineLogging():
    # Define the logger and the entry string (here "FileHandling") within the log file
    import sys
    sys.path.insert(0, '../logging/')
    from logutilities import logger
    log = logger.getLogger("FileHandling")
    return log


# call this *.py-file with:
# python filehandling.py /path-to-your-folder/to-be-watched-for
if __name__ == "__main__":
    log = defineLogging()
    main(sys.argv)

    