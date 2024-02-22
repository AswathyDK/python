n=11
for i in range(n):
    for j in range(n):
        if ((i-j>=0 and i+j<=n-1)or (i-j<=0 and i+j>=n-1)):
            print("*",end='')
        else:    
            print(end='')  
    print()           
    