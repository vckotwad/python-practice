#method overloading is not supported ny python only last method is executed 
class test:
    def m1(self):
        print("no arguments")
    def m1(self,x):
        print(" 1 argument method")
    def m1(self,x,y):
        print("2 argument method")

t1=test()
#t1.m1() not valid
#t1.m1(10) not valid
t1.m1(10,20)