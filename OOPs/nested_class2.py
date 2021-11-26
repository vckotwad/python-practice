#creatin person class and inner class dob
class person:
    def __init__(self,name,dd,mm,yyyy):
        self.name=name
        print("person object creation done")
        self.dob=self.dob(dd,mm,yyyy)
    def info(self):
        print("name is {}".format(self.name))
        self.dob.display()
    class dob:
        def __init__(self,dd,mm,yyyy):
            self.dd=dd
            self.mm=mm
            self.yyyy=yyyy
            print("dob object creation done")
        def display(self):
            print("dob is {}/{}/{}".format(self.dd,self.mm,self.yyyy))


p=person('vaibhav',1,2,1995)
p.info()
