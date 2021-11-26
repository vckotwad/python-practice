#decorator demo
def decor(func):
    def inner():
        print("this is modiefied extended function")
    return inner
@decor # by using decorator display will be used as argument to decor functino and inner function will be returned or executed
def display():
    print("this original function ")

display()