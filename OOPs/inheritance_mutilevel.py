#multilevel
print("mutilevel inheritance")
class a:
    def m3(self):
        print("this is grand parent class")
class b(a):
    def m4(self):
        print("this is parent method")
class c(b):
    def m5(self):
        print("this is child method")
    
child=c()
child.m3()
child.m4()
child.m5()