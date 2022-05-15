import os
import shutil
source=input("Enter The Source Folder You Wish To Organise ")
destination=input("Enter The Destination You Wish To Organise ")
source+='/'
destination+='/'
ListOfFiles=os.listdir(source)
for file in ListOfFiles:
    shutil.copy((source+file),destination)