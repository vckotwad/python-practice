#super() is used to explicitely calling prent class methods, variables etc....
class p:
    a=10
    def __init__(self):
        print("this is parent constructor")
    def m1(self):
        print("this is parent instance method")
    @classmethod
    def m2(cls):
        print("this is parent clss method")
    @staticmethod
    def m3():
        print("this is parent static method ")

class c(p):
    def __init__(self):
        print("this is child constructor")
    def m1(self):
        print(super().a)
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
child=c()
child.m1()
    