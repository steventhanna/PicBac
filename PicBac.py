import os, sys, shutil

# Constants
# The source file to scan
source = "/Users/steventhanna/desktop/work"
# The destination drive to copy
destination = "/Users/steventhanna/desktop/testing"


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
    for file in dirs:
        print file
        print isPicture(file)
        if os.path.isdir(file) == True:
            walkAndCopy(file)
        else:
            print os.path.abspath(file)
            if isPicture(file) == True:
                shutil.copyfile(file, destination)


def isPicture(fileName):
    if os.path.isdir(os.path.abspath(fileName)) == True:
        return False
    extensions = {"png", "jpg", "jpeg", "gif", "tiff"}
    extend = os.path.abspath(fileName)
    extendArr = extend.split("/")
    finalName = extendArr[len(extendArr) - 1]
    extendArr2 = finalName.split(".")
    extendFinal = extendArr2[len(extendArr2) - 1].lower()
    print "EXTEND: " + extendFinal
    for fileType in extensions:
        if(fileType == extendFinal):
            return True
    return False

if __name__ == "__main__":
    main()
