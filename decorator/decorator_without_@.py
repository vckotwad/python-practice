def decor(func):
    def inner():
        print("decor function executed")
    return inner

def test():
    print("original function executed")

t=test()
dt=decor(test) #getting inner decor function 
dt() #executing decor functino without @decor