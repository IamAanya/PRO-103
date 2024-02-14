import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

fromdir="./source"
todir="./destination"

dirtree={
    "ImageFiles":['.gif','.png','.jpg','.jpeg'],
    "VideoFiles":['.mpg','.mp4','.mpv'],
    "DocumentFiles":[".ppt",".xls",".pdf",".txt",".csv"],
    "Setup":[".ext",".bin"]
}
class FileMovementHandler(FileSystemEventHandler):
    def on_created(self,event):
        name,extension=os.path.splitext(event.src_path)
        time.sleep(1)

        for key,value in dirtree.items():
            time.sleep(1)
            
            if extension in value:
                filename=os.path.basename(event.src_path)

               
                path1=fromdir+"/"+filename
                path2=todir+"/"+key
                path3=todir+"/"+key+"/"+filename

                if os.path.exists(path2):
                    print("creating")
                    shutil.move(path1,path3)
                    time.sleep(1)
                else:
                    os.makedirs(path2)
                    shutil.move(path1,path3)  
                    time.sleep(1)  
eventHandler=FileMovementHandler()
observer=Observer()
observer.schedule(eventHandler,fromdir,recursive=True)
observer.start()
try:
    while True:
        time.sleep(2)
        print("running")
except KeyboardInterrupt:
    print("stop")
    observer.stop()        

