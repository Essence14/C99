import os
import shutil
from unicodedata import name
path=input("Enter The Path You Wish To Organise ")
ListOfFiles=os.listdir(path)
for file in ListOfFiles:
    name,ext=os.path.splitext(file)
    ext=ext[1:]
    if ext=="":
        continue
    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
    else:
        os.mkdir(path+'/'+ext)
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
