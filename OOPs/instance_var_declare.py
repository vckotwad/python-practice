#no of instance variable places

class test:
    def __init__(self): #inside constructor
        self.a=10
        self.b=20

    def m1(self): #inside instance method
        self.c=30

    def display(self):
        print("inside class", self.a,self.b,self.c)

    def delet(self):
        del self.c

t1=test()
t1.m1()
t1.d=40 #outside class
print(t1.__dict__)
t1.display()
print("outside class", t1.a,t1.b,t1.c)
del t1.a,t1.b
t1.delet()
print(t1.__dict__)
