#function as argument
def f1(fun):
    fun()
def f2():
    print("f2 function is executing")
f1(f2) # f2 is passed as an argument to f1