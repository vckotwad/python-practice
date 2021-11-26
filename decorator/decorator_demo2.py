#decorator demo

def smartdiv(func):
    def inner(a,b):
        if b==0:
            print("you can not divide by zero")
        else:
            func(a,b)
    return inner

@smartdiv
def div(a,b):
    print(a/b)

div(10,2) 
div(10,0)