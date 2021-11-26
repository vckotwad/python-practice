class a:
    def m1(self):
        print("a method")
class b(a):
    def m1(self):
        print("b method")
class c(b):
    def m1(self):
        print("c method")
class d(c):
    def m1(self):
       super(c,self).m1() #parent of of is b so b's method will be executed
       #b(self).m1() #this will also works
D=d()
D.m1()

