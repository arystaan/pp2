import re

txt = "mvfdkFdkcdovdoDdsmcosdmocEockdok"
print(re.findall("[A-Z]{1}[a-z]+", txt))
