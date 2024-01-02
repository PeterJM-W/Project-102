import os
import shutil

fromDir = "/Users/imac27/Downloads"
toDir = "/Users/imac27/Downloads/Document_Files"

listOfDocs = os.listdir(fromDir)

for fileName in listOfDocs:
    name, exten = os.path.splitext(fileName)

    if exten == "":
        continue
    
    if exten in [".txt", ".doc", ".docx", ".pdf"]:
    
        path1 = fromDir + "/" + fileName
        path2 = toDir + "/" + "Document_Files"
        path3 = toDir + "/" + "Document_Files" + "/" + fileName

        if os.path.exists(path2):
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            shutil.move(path1, path3)