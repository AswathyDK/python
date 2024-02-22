n=int(input("number"))
m=int(input("number"))
def len(n):
    c=0
    while n:
        n=n//10
        c=c+1
    return c     
def zfill(c):
    a=1
    while c:
        a=a*10
        c=c-1
    return a
def temp(n,m):
    f=1
    if n<0:
        n=n*-1
        f=-1
    if m<0:
        m=m*-1    
    return f*(n*zfill(len(m))+m)

print(temp(n,m))
#OUTPUT=number23412
#number77
#2341277
