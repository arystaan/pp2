import os
with open('blablabla.txt', 'r') as f:
    x = sum(1 for i in f)
print(x)