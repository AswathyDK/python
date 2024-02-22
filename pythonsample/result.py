from packagegra import circle as c
from packagegra import rect as r
import file
n1=int(input("enter the radious"))
b=c.area(n1)
d=c.peri(n1)
print(b)
print(d)
x=int(input("enter the length"))
y=int(input("enter the bradth"))
a=r.area(x,y)
print(a)
b=r.vol(x,y)

print(b)