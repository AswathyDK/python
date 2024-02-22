class Cubo:
    def __init__(self,length,breadth,hight):
        self.length=length
        self.breadth=breadth
        self.__hight=hight
    def disp(self):
        print("length=",self.length) 
        print("breadth=",self.breadth)
        print("hight=",self.__hight)
    def calc(self):    
        return self.length*self.breadth*self.__hight 
 
class Volume(Cubo):
    
    def disp(self):
        super().disp()
        super().calc()
    def __gt__(self,other):
        return self.calc()>other.calc()


r1=Volume(2,3,1)
#r1.calc(2,3,1)
r2=Volume(0,3,1)
#r2.calc(7,3,1)
if r1>r2:
    print("r1")
else:
    print("r2")                       