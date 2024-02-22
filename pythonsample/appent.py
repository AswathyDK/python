import re
f=open("pp.txt",'r')
line=f.read()
p="\d{2}+[A-Z]{3}+\d{3}"
m=re.findall(p,line)
print(m)
f.close();