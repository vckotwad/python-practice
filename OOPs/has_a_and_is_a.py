#using both has a and is a in single program
class car:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def carinfo(self):
        print("car name is {} and color is {}".format(self.name,self.color))
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print("i am eating")
class employee(person):
    def __init__(self,name,age,sal,car):
        self.name=name #instead of using this super().__init__(name,age) , parent class constructor can be called
        self.age=age
        self.sal=sal
        self.car=car
    def work(self):
        print("I am working on python")
    def empinfo(self):
        print(self.name)
        print(self.age)
        print(self.sal)
        self.car.carinfo()

car=car("suzuki","white")
emp=employee('vaibhav',27,10000,car)
emp.work()
emp.empinfo()
