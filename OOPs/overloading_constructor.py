#constructor overloading
class test:
    def __init__(self, a=None, b=None): #default arguments
        print("default arg constructor")
    def __init__(self, *args): #variable length arguments
        print("variable length arg constructor")
t=test() 