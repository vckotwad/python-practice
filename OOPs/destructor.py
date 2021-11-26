#destructor
from time import sleep
class test:
    def __init__(Self):
        print("obhect is initialised")
    def __del__(self):
        print("destroying object")

t1=test()
t2=test()
t1=None
print("end of apllication")