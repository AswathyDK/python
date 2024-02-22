f=open("pp.txt",'r')
lines=f.readlines()
f.close()
for line in lines:
    m=len(line)
    print(m)