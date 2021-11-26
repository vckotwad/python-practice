class student:
    '''this class developed by vaibhav'''
    #any variables
    #any methods
    def __init__(self):
        self.name='vaibhav'
        self.roll=101
        self.marks=75
    def talk(self):
        print("my name is {}, my roll no is {}, my marks are {}".format(self.name,self.roll,self.marks))
s=student() #object created with ref variable s
print(s.name) #calling variable of object using reference variables


s.talk() #student class method is called