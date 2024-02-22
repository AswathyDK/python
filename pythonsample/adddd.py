class Add:
    def __init__(self,num1):
        self.num1=num1
        
    def __add__(self,other):
        c=self.num1+other.num1
        print("sum=",c)
r1=Add('hello')
r2=Add('world')
r1+r2        

