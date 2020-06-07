import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import json

import sys
sys.path.insert(0, '../flask/src/')

import flask_client as fc
import logutilities

#show current working directory
#pwd

# Define the logger and the entry string (here "filehandling") within the log file
logging = logutilities.logger.setLoggerName("filehandling")

class EventHandler(FileSystemEventHandler):
    file_cache = {}

    def on_created(self, event):
        seconds = int(time.time())
        key = (seconds, event.src_path)
        print("Key: %s" %str(key))
        if key in self.file_cache:
            logging.debug("already registered event")
            return
        self.file_cache[key] = True
        
        # Process the file
        file = event.src_path
        processFile(event, file)
    
    #def on_any_event (if everything should be traced)
    #...

def processFile(event, file):
    logging.info("Trying to process file: %s" %file)
    try:
        with open(file, mode="r") as json_file:
            content = json_file.read()
            logging.info("Opened json-file with this content: %s" %content)
            
    except ValueError as err:
        logging.error("Error while reading file:", exc_info=True)
        return

    try:
        #load rawdata and create string with correctly formated JSON - with double quotes
        #{'a':1} --> {"a":1}
        rawdata = json.loads(content)
        data = json.dumps(rawdata)
    except ValueError as e:
        logging.error("Invalid Json Format:", exc_info=True)
        return False
    
    logging.info("sending data from filewatcher to client")
    fc.sendPayload(data)

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
    logging.info("Watching at: %s ..." % path)
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
        

# call this *.py-file with:
# python filehandling.py /path-to-your-folder/to-be-watched-for
if __name__ == "__main__":
    main(sys.argv)

    