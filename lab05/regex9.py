import re

txt = "icmds Mkdco moemc Pxskmcmks"
pattern = re.compile(r'([A-Z])')
print(pattern.sub(r' \1', txt).strip())