import os
lst = list(input().split())
with open('blablabla.txt', 'w') as f:
    for i in lst:
        f.write(str(i)+'\n')
