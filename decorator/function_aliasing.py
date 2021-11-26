#function aliasing
def wish():
    print("hello how are ")
greet=wish #now greet direct to same object as wish
print(id(wish))
print(id(greet))
greet()
wish()
del wish
greet()  