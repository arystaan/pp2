import os
path = os.getcwd()
def checkForExistence(some_path):
    if os.access(some_path, os.F_OK):
        print(os.listdir(path))
    else:
        print("Given path doesn't exist")
checkForExistence(path)