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


if __name__ == "__main__":
    path = "/path-to-your-dir/temp"
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