#operator overloading
class book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other): #using magic mathod for add
        return book(self.pages+other.pages) #returning book object instead of int so that operand must be same
    def __str__(self):
        return 'the total no of pages {}'.format(self.pages)
    def __gt__(self,other):
        return self.pages>other.pages
b1=book(100)
b2=book(200)
b3=book(300)
b4=book(500)
#print(b1+b2)
#print(b1>b2)
#print(b1<b2) #python automatically reverse functionality
print(b1+b2+b3+b4)
