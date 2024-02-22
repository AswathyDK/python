import re
f=open("tt.txt",'r')
line=f.read()
m=re.sub(r'[0-9]','&',line)
print(m)