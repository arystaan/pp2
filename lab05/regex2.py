import re

txt = "vhvcnwlcicjfvmabbbfmivmwcl"
print(re.search("a{1}b{2,3}",txt))