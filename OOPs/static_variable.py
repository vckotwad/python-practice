#declaring static variables
class test():
    a=10  #inside class
    def __init__(self):
        test.b=20 #inside constructor

        
        print(self.a)
    def m1(self):
        test.c=30 #inside instance method
        print(self.b)
    @classmethod
    def m2(cls):
        cls.d=40 #inside class method
        test.e=50
        del cls.b #deleting static variable using cls
        cls.e=90 #modiying static variable using cls or class name
        print(cls.d,test.e)
    @staticmethod
    def m3():
        test.f=60 #insde static method
        print(test.f)

t=test()
t.m1()
t.m2()
t.m3()
test.g=70
print(test.g,t.g)
del test.a #deleteing static var using class name
test.a=300 #value of static variable will changed only by using classname or cls
print(t.a)