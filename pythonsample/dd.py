import re
f=open("apple2.txt",'r')
line=f.read()
pattern = "\d{2}-\d{2}-\d{4}"
m=re.findall(pattern,line)
print(m)
f.close()