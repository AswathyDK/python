class Time:
    def __init__(self,hour,minute,secont):
        self.__hour=hour
        self.__minute=minute
        self.__secont=secont
    def __add__(self,other):
        a=self.__hour+other.__hour
        print("hour=",a)
        b=self.__minute+other.__minute
        print("minute=",b)
        c=self.__secont+other.__secont
        print("secont=",c)
r1=Time(2,25,5)
r2=Time(1,30,10)
r1+r2        
        