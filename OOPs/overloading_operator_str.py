#__str__ overloading
class a:
    def __init__(self,name):
        self.name=name
    def __str__(self): #overloading str
        return self.name
k=a('vaibhav')
print(k)