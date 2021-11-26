class school:
    schooln='abc' 
    def __init__(self,name):
        self.name=name

    def info(self): #instance method , using instance variables
        print(self.name)

    @classmethod   #classmethod using class or static variables
    def schoolinfo(cls):
        print(cls.schooln)

    @staticmethod   #static method , not using any variables, general utility method
    def sum(a,b):
        print(a+b )    

s=school('vaibhav')
s.info()   
s.schoolinfo()
s.sum(10,20)
