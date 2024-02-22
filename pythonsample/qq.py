n=int(input("number"))
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
def temp(n):
   
        
         a=n%zfill(len(n)-1)
         print(a)
print(temp(n))
#OUTPUT=number23412
#number77
#2341277       