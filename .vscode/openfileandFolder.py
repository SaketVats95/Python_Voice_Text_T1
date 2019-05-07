import os

string_dirName = input()
string_dirName = string_dirName.replace(
    "drive", ":\\").replace("then", "\\").replace(" ", "")
f = []
fileNames = []
dirPath = ""
for (dirpath, dirnames, filenames) in os.walk(string_dirName):
    fileNames.extend(filenames)
    # fileNames.extend(dirpath+"\\"+dirnames)
    dirPath = dirpath
    break
count = 0
for info in fileNames:
    count += 1
    print(count+":"+info)
openFile_Number = int(input())
openFile_Name = fileNames[openFile_Number-1]
os.startfile(dirPath+"\\"+openFile_Name)
