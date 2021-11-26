#function as return value
def outer():
    def inner():
        print("how are you")
    return inner #no parenthesis. it will  return the object of inner , if parentheses then first inner will be executed and return the inner function value
f=outer() #now f will direct to same object at inner. 
f() #inner object called by using f()