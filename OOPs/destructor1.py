#destructor:
class test():
    def __init__(self):
        print("creating object")
    def __del__(self):
        print("destroying object")
l=[test(),test(),test()]

del l
from time import sleep
sleep(3)
print("end of application")