# PicBac
# Steven Hanna

import os, sys, shutil, time

# Constants for user to edit
# The source file to scan
source = "EDIT_SOURCE"
# The destination drive to copy
destination = "EDIT_DESTINATION"

# File counter
fileCounter = 0;


def main():
    # Make sure destination is available
    if os.path.exists(destination):
        dirs = os.listdir(source)
        walkAndCopy(source)
    else:
        print "DESTINATION NOT ACCESSIBLE"


def walkAndCopy(folder):
    dirs = os.listdir(folder)
    for fileName in dirs:
        if os.path.isdir(folder + "/" + fileName) == True:
            walkAndCopy(folder + "/" + fileName)
        else:
            if isPicture(folder + "/" + fileName) == True:
                copyFile(folder + "/" + fileName, destination + "/" + fileName)

def copyFile(src, dest):
    # Check if the file already exists
    global fileCounter
    if os.path.isfile(dest) == True:
        # Determine last modified date
        destMod = time.ctime(os.path.getmtime(dest))
        srcMod = time.ctime(os.path.getmtime(src))
        if srcMod < destMod:
            # The src file is the newest file
            # Copy the src file to the destination file
            shutil.copyfile(src, dest)

            fileCounter += 1
            print "Amount of Files Copied: ", fileCounter
    else:
        shutil.copyfile(src, dest)
        fileCounter += 1
        print "Amount of Files Copied: ", fileCounter

def isPicture(fileName):
    if os.path.isdir(os.path.abspath(fileName)) == True:
        return False
    else:
        extensions = {"png", "jpg", "jpeg", "gif", "tiff"}
        extend = os.path.abspath(fileName)
        extendArr = extend.split("/")
        finalName = extendArr[len(extendArr) - 1]
        extendArr2 = finalName.split(".")
        extendFinal = extendArr2[len(extendArr2) - 1].lower()
        for fileType in extensions:
            if(fileType == extendFinal):
                return True
        return False

if __name__ == "__main__":
    main()
