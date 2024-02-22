class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
        
        
    def __lt__(self,other):
       return self.area() < other.area()
r1=Rectangle(2,3)
r2=Rectangle(4,1)
if r1 < r2:
    print("first less")
else:
    print("second grater")            