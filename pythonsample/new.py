n=int(input("enter the number"))
m=int(input("enter the number"))
def len(n):
    c=1
    while n<0:
        n=n//10
        c=c+1
        print(c) 
len(n)           