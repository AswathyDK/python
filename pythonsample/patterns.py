n=11
for i in range(n):
    for j in range(n):
        if    j==0  or j==n-1 or i+j==n-1 or i==j or i-j>=0 and i+j<=n-1 or i-j<=0 and i+j>=n-1 :#j==n//2:
            print("*" ,end='')
        else:
            print(end=' ')
    print()            