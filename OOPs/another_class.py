#accesssding members of one class inside another class
class employee:
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal
    def display(self):
        print("name is {} salary is {}".format(self.name,self.sal))


class manager:
    def updatesal(emp):
        emp.sal=emp.sal+10000
        emp.display()

emp=employee('vaibhav',45000)
manager.updatesal(emp)