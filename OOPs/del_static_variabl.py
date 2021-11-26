class test:
    a=10
    def __init__(self):
        del test.a
        test.b=20
    def m1(self):
        del test.b
        test.c=30
    @classmethod
    def m2(cls):
        del cls.c
        cls.d=40
    @staticmethod
    def m3():
        del test.d
        test.e=50
t=test()
t.m1()
t.m2()
t.m3()
del test.e
print(test.__dict__)

