n=11
for i in range(n):
    for j in range(n):
        if   i+j<=n//2 or i-j>=n//2:
            print("*",end='')
        else:
            print(end='')
    print()            