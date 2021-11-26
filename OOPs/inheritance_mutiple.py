#mulitple inheritance
print("this is multiple inheritance")
class p1:
    def m1(self):
        print("parent 1 method ")
class p2:
    def m2(self):
        print("parent 2 method")
class c(p1,p2): #order is imp for accessing same method name #diamond access problem with same method name
    def m3(self):
        print("child method")

C=c() 
C.m1()
C.m2()
C.m3()