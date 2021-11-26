# multiplication overloading
class employee:
    def __init__(self,sal):
        self.sal=sal
    def __mul__(self,other): #operator loverloading
        return self.sal*other.time
class time:
    def __init__(self,time):
        self.time=time
e=employee(1000)
t=time(25)
print("this month salary is",e*t)
