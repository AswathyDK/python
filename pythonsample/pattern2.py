n=int(input("enter the num"))
for i in range(1,n+1):
    for j in range(1,n):
        if i-j==n:
            print("*",end='')
    print()        