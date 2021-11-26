#has a relationship
class car:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def carinfo(self):
        print("car name is {} and color is {}".format(self.name,self.color))

class employee:
    def __init__(self,name,car):
        self.name=name
        self.car=car
    def empinfo(self):
        print("employee name is {} ".format(self.name))
        self.car.carinfo()

car=car('suzuki','white')
emp=employee('vaibhav',car)
emp.empinfo()