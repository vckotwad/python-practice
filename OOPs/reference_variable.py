import sys
class test:
    pass
t1=test()
t2=t1
print(sys.getrefcount(t1)) #self and t1 so ans is 2
