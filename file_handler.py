from datetime import datetime
from watchdog.events import FileSystemEventHandler
from mqtt_publisher import Publisher

class FileHandler(FileSystemEventHandler):
        
    def on_modified(self, event):
        publisher = Publisher()

        is_dir = 'directory' if event.is_directory else 'file'
        log = str(datetime.now()) + " Modified " + is_dir + " -> " + event.src_path

        messages = [{'topic':"test", 'payload': self.read_file(event.src_path)}, 
                    ("test", log, 0, False)]

        publisher.publishMultiple(messages, hostname="localhost")
        #publisher.publishSingle("test", log)

    def read_file(self, path):
        file = open(path)
        file_string = file.read()
        byte_array = bytes(file_string)
        return byte_array