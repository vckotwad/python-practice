#nested methods
class math:
    def m1(self,a,b):
        def add(a,b):
            print("sum is ",a+b)
        add(a,b) #calling add function which inside m1

t=math()
t.m1(10,20) #proving values to m1 which passes add function


