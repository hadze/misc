import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import sys
sys.path.insert(0, '../flask/src/')
import flask_client as fc
#show current working directory
#pwd

class EventHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        fc.sendPayload()
        print(event)

def checkParameters(params):
    print("Number of arguments: ", len(sys.argv))
    print("The arguments are: " , str(sys.argv))
    if len(sys.argv) >= 2:
        print("Path to be watched at is: %s" %str(sys.argv[1]))
        path = str(sys.argv[1])
        return path
    else:
        print("Path not provided!")
        return 0



if __name__ == "__main__":
    res = checkParameters(sys.argv)
    if res == 0:
        print("Closing application...")
        sys.exit()
    
    path = res
    print("Watching at: %s ..." % path)
    #path = "/Users/arminhadzalic/Dokumente/_armin"
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