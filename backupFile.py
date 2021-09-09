import os 
import shutil
source = input("Enter source folder name: ")
dest = input("Enter destination folder name: ")
source = source+'/'
dest = dest+'/'
listOfFiles = os.listdir(source)
for file in listOfFiles:
    shutil.copy((source+file) , dest)