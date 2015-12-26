import os, sys, shutil, time

# Constants
# The source file to scan
source = "/Users/steventhanna/desktop/work"
# The destination drive to copy
destination = "/Users/steventhanna/desktop/testing"

# File counter
fileCounter = 0;


def main():

    # Open a file
    path = "/Users/steventhanna/desktop"
    dirs = os.listdir(source)
    walkAndCopy(source)

    # This would print all the files and directories
    # for file in dirs:
        # print file



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
    if os.path.isfile(dest) == True:
        # Determine last modified date
        destMod = time.ctime(os.path.getmtime(dest))
        srcMod = time.ctime(os.path.getmtime(src))
        if srcMod < destMod:
            # The src file is the newest file
            # Copy the src file to the destination file
            shutil.copyfile(src, dest)
            global fileCounter
            fileCounter += 1
            print "Amount of Files Copied: ", fileCounter
        #
        # # Ask the user what to do
        # fileArr = dest.split("/")
        # print "The file: " + fileArr[len(fileArr) - 1] + " already has been copied onto the drive."
        # print "1. Replace File 2. Keep Both Files"
        # response = raw_input()
        # if response == "1":
        #     shutil.copyfile(src, dest)
        #     global fileCounter
        #     fileCounter += 1
        #     print "Amount of Files Copied: ", fileCounter
        # elif response == "2":
        #     copyFile(src, dest + "_copy")
        # else:
        #     print "Invalid input."
        #     copyFile(src, dest)
    else:
        shutil.copyfile(src, dest)
        global fileCounter
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
