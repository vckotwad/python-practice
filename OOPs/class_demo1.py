class student:
    def __init__(self,name,marks,roll):
        self.name=name
        self.marks=marks
        self.roll=roll

    def talk(self):
        print('*'*30)
        print("hello my name is {} , \n my marks are {} \n and my roll no is {}".format(self.name,self.marks,self.roll))

s1=student('vaibhav',90,1)
s2=student('sumedh',95,2)

s1.talk()
s2.talk()

