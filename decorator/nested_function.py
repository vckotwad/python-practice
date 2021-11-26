#nested function
def outer():
    print("outer function executino starte")
    def inner(): #function declared inside
        print("innner function is executing")
    inner() #function called inside
    print("outer function execution completed")
outer()
