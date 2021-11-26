#person and employee


class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print("i am eating")
class employee(person):
    def __init__(self,name,age,sal):
        self.name=name #instead of using this super().__init__(name,age) , parent class constructor can be called
        self.age=age
        self.sal=sal
    def work(self):
        print("I am working on python")
    def empinfo(self):
        print(self.name)
        print(self.age)
        print(self.sal)

e=employee('vaibhav',27,10000)
e.eat()
e.work()
e.empinfo()