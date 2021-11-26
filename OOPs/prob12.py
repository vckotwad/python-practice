#program to track no objects created in class
class student:

    c=0 #defining static variable

    def __init__(self,name):
        self.name=name
        student.c=student.c+1 #for every object creation count will increase
    
    @classmethod
    def obj(cls):
        print(cls.c) #printing no of objects created

s1=student('vaibhav')
student.obj()
s2=student("akash")
s2.obj()

