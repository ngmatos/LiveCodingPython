import paho.mqtt.client
from watchdog.events import FileSystemEventHandler

class FileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print "Got it!"