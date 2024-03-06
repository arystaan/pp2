import os
path = os.getcwd()
print(f"Check for accessibility:\nExistence: {os.access(path, os.F_OK)} \nReadability: {os.access(path, os.R_OK)} \nWritability: {os.access(path, os.W_OK)} \nExecutability: {os.access(path, os.X_OK)}")