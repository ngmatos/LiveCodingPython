import os
import sys
sys.path.append('./file_readers')
sys.path.append('./mqtt')
from file_reader import FileReader

from datetime import datetime
from watchdog.events import FileSystemEventHandler
#from watchdog.events import PatternMatchingEventHandler
from mqtt_publisher import Publisher

class EventHandler(FileSystemEventHandler):
    
    def on_modified(self, event):
        publisher = Publisher()
        reader = FileReader(event.src_path)        

        if not event.is_directory and not str(os.path.basename(event.src_path)).startswith('.'):

            print('passei')

            is_dir = 'directory' if event.is_directory else 'file'
            log = str(datetime.now()) + " Modified " + is_dir + " -> " + event.src_path

            messages = [{'topic':"test", 'payload': "<!SOF!>\n" + reader.read_file() + "\n<!EOF!>"}, 
                        ("test", log, 0, False)]

            publisher.publishMultiple(messages, hostname="localhost")
        else:
            return