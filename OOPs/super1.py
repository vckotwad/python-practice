class person:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(self.name)
class child(person):
    def __init__(self,name,age):
        super().__init__(name) #usin parent class constructor for defing instance variables
        self.age=age
    def display(self):
        super().display()
        print(self.age) #using parent class display method for displaying half the properties
c=child('vaibhav',27)
c.display()