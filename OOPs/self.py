#self
class student:
    def __init__(self):
        print("adr of self is ",id(self))
        
s=student()
print('adr of s reference variable is',id(s))