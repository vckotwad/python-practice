class test:
    def m1(self,a=None,b=None):
        print("default variable length")
    def m2(self, *args): #args will be a tuple
        print("changing *args method")
t=test()
t.m1()
t.m2(10,20,30,40)
