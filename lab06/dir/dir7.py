import os
f = open('blablabla.txt', 'r')
with open('copy_file.txt', 'w') as file:#or 'a'
    for x in f:
        file.write(x)

f.close()