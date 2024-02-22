import re
f=open("pp.txt",'r')
line=f.read()
pattern="[a-zA-Z0-9]{8}"
m=re.findall(pattern,line)
print(m)
f.close()