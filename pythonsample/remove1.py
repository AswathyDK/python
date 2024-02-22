inf=open("ee.txt",'r')
infile=open("tt.txt",'w')
line=inf.readlines()
infile.writelines(line)
print("copied")
inf.close()

