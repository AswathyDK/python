class Student:
    def __init__(self,name,mark1,mark2):
        self.name=name
        self.mark1=mark1
        self.mark2=mark2

   # def sum(self):
      #  return  self.mark1+self.mark2
    def __gt__(self,other):
        return self.sum()>other.sum() 
    def __add__(self,other):
        a= self.sum()+other.sum()
        print(a)
r1=Student("aswathy",25,30)
r2=Student("achu",30,13) 
#graterthan
if r1>r2:
    print("aswathy")
else:
    print("achu")
    #addition  
#r1+r2                  