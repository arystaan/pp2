import re

txt = "jivwcmvnm..,,  "
pattern = r"[ ,.]"
x = re.sub(pattern, ":", txt)
print(x)