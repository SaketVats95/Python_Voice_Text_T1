import os

strr="open C drive  SaketShare"

def OpenFIleandFolder(data):
    print(data)
    string_dirName = data
    string_dirName = string_dirName.replace(
        "drive", ":\\").replace("then", "\\").replace(" ", "").replace("open","")
    print(string_dirName)
    open(string_dirName)
    #f = []
    #fileNames = []
    #dirPath = ""
    #for (dirpath, dirnames, filenames) in os.walk(string_dirName):
     #   fileNames.extend(filenames)
        # fileNames.extend(dirpath+"\\"+dirnames)
      ## break
    #count = 0
    ##   count += 1
      #  print(count , ":" ,info)
    #openFile_Number = int(input())
    #openFile_Name = fileNames[openFile_Number - 1]
    #os.startfile(dirPath + "\\" + openFile_Name)


OpenFIleandFolder(strr)