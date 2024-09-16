import sys
import time
from watchdog.observers import Observer 
from watchdog.events import LoggingEventHandler
import logging
import getpass
import os
import shutil

#Backup directory to another folder

def on_modified(event):     
        #Backup by copy directories from one to another folder
        backup_path = '/Users/anonymous/Desktop/CYBER/Watchdog/Backup'
        #Fetch all files in the path
        for file_name in os.listdir(path):
            source = os.path.join(path, file_name)
            destination = os.path.join(backup_path, file_name)
            if os.path.isfile(source):
                shutil.copy(source, destination)
                print(f"Copied: {file_name}")

if __name__ == '__main__':
    user = getpass.getuser()
    logging.basicConfig(
        filename= 'dev.log',    #store logs to a file
        filemode='a',
        level=logging.INFO, 
        format='%(asctime)s | %(process)d | %(message)s' + f' userid:{user}',
        datefmt= '%Y - %m - %d %H:%M:%S')
    #Directory of File to be Monitored
    path = sys.argv[1] if len(sys.argv)>1 else '.'
    print(path)

    event_handler = LoggingEventHandler()
    event_handler.on_modified = on_modified
   
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop() #stop observing
        observer.join() #wait observer finish remaining task before terminate program