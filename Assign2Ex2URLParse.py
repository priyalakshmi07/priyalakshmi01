import re

s=input("Enter the Email id:")

host = re.findall('://([\w\-\.]+)', s)
separator=""
print("Host name:",separator.join(host))

port=re.findall('[\d]+',s)
separator=""
print("port:",separator.join(port))

protocol=re.findall('(\w+)://',s)
separator=""
print("protocol:",separator.join(protocol))
