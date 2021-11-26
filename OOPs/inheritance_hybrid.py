#hybrid inheritance

class GP():
    def m0(self):
        print("this is grand parent method")
class P1(GP):
    def m1(self):
        print("this is parent 1")
class P2(GP):
    def m2(self):
        print("this is parent 2")
class C1(P1,P2):
    def m3(self):
        print("this is child 1")
class C2(P1,P2):
    def m4(self):
        print("this is child 2")

c1=C1()
c2=C2()
c1.m0()
c1.m1()
c1.m2()
c1.m3()
c2.m0()
c2.m1()
c2.m2()
c2.m4()

