#single inheritance
print("single inheritance")
class p:
    def m1(self):
        print("this is parent class")
class c(p):
    def m2(self):
        print("this is child class")

child=c()
child.m1()
child.m2()


