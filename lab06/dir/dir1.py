import os
path = os.getcwd()
print("only directories:", [dire for dire in os.listdir(path) if os.path.isdir(dire)])
print("only files:", [file for file in os.listdir(path) if os.path.isfile(file)])
print("all dir and files:", os.listdir(path))
