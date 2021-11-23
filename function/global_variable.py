a=10 #global variable declared ouside function
def f1():
    global a #changes values of global variable inside functionf
    a=20
    print(a)
def f2():
    a=50
    print(globals().get('a')) #globals()) is accessing all global variables in program
    print(globals()['a']) #globals()) is accessing all global variables in program
f1()
f2()

