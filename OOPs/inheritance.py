#inheritance basic
class parent:
    a=10
    def __init__(self):
        print("this is parent constructor")
        self.b=20
    def m1(Self):
        print("this is a parent instance method")
    @classmethod
    def m2(cls):
        print("this is a parent class method")
    @staticmethod
    def m3():
        print("this is a parent static method")
class child(parent):
    def m4(self):
        print("this is a child method")
c=child()
c.m1()
c.m2()
c.m3()
c.m4()
print(c.a)
print(c.b)