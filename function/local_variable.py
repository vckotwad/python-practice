a=5 # global variable available for all functions
def f1():
    print(a)
def f2(): 
    a=20 # local variable access only in this function
    print(a)
f1()
f2()

