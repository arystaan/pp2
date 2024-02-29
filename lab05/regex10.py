import re

txt = 'vvmfvfkKkodmoJcmdiLimvfi'
pattern = re.compile('(?=[A-Z])')
x = pattern.sub('_', txt).lower()

print(x)
