import re
f=open("ee.txt",'r')
line=f.read()
pattern="[0-9a-zA-z]+@[0-9a-zA-z]+.com+"
m=re.findall(pattern,line)
print(m)
f.close()