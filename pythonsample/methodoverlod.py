class Rect:
    def area(self,l,b,c='non',):
        self.l=l 
        self.b=b
        self.c=c
        if c==0:
            a=self.l*self.b
            print(a)
        else:
            b=self.l*self.b*self.c    
            print(b)
r=Rect()
r.area(2,3)

   