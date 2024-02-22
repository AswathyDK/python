class Trian:
    def __init__(self,length,hight):
        self.lenght=length
        self.hight=hight
    def disp(self):
        print("length=",self.lenght) 
        print("hight=",self.hight)
class Area(Trian):
    def calc(self,lenght,hight):
        super().__init__(lenght,hight)
        return self.lenght*self.hight
    def __lt__(self,other):
        return self.calc()<other.calc()
r1=Area(4,3)
print("r1=",r1)
r2=Area(2,1)
print("r2",r2)
if r1<r2:
    print("equal")
else:
    print("not equal")        
    

