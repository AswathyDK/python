class Publisher:
    def __init__(self,name):
        self.name=name
    def disp(self):
        print("name=",self.name)
class Book(Publisher):
    def __init__(self,title,author,name):
        super().__init__(name)
        self.title=title
        self.author=author
    def disp(self):
        super().disp()
        print("title=",self.title)
        print("author=",self.author)
class Python(Book):
    def __init__(self,price,pgno,title,author,name):
        super().__init__(title,author,name)
        self.price=price
        self.pgno=pgno
    def disp(self):
        super().disp()
        print("price=",self.price)
        print("pagnumber=",self.pgno)
r=Python("abc","fgh","stert",125,50)
r.disp()        

