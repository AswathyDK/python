class Area:
    def __init__(self,l,h):
        self.l=l
        self.h=h
    def find(self):
         return self.l*self.h      
class Calc(Area):
    def vol(self,l,h,b):
        super().__init__(l,h)
        self.b=b
    def __gt__(self,other):
        return self.find()>other.find()
r1=Calc(2,3)
r2=Calc(5,6)
if r1>r2:
    print("grater")
else:
    print("not grater")            