#decorator demo
def decor(func):
    def inner(a,b):
        print("#"*30)
        print("the sum is ")
        func(a,b) #using original function also. add will be at the name of fucn... 
        print("#"*30)
    return inner
@decor
def add(a,b):
    print(a+b)

add(10,20)
