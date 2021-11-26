#public,private,protected members
class test:
    def __init__(self):
        self.x=10 #public variable
        self_x=20 #protected variable
        self__x=10 #private variable
    def m1(self): #public method ,access inside and outside class
        pass
    def _m1(self): #proteced method access inside class and child class
        pass
    def __m1(self): #private method, access only inside class no outside
        pass
t=test()
t.m1()
#t.__m1() attribute error, name mangling can be used to access