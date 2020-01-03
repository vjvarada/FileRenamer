import os

if __name__ == "__main__":

    folderName = raw_input("Enter Path of Folder to change names within: ")
    oldChar = raw_input("Enter Characters to replace in File Names: ")
    newChar = raw_input("Enter Characters to replace with in File Names: ")
    filesPaths = []


    for (root,dirs,files) in os.walk(folderName):
        for file in files:
            filesPaths.append(os.path.join(root,file))
    print 'Files Changed: \n'
    for path in filesPaths:
        newname = path.replace(oldChar, newChar)
        if newname != path:
            os.rename(path, newname)
            print newname

