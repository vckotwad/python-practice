#decorator chaining

def decor1(func):
    def inner1():
        print("decor 1 execution")
    return inner1
def decor2(func):
    def inner2():
        print("decor 2 execution")
    return inner2
@decor2 #from bottom to top but only last output will be executed
@decor1
def f():
    print("original function execution")
f()
