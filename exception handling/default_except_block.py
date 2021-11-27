#default except block
try:
    x=int(input("enter the first number"))
    y=int(input("enter the second number"))
    print(x/y)
except ZeroDivisionError as z:    #order of except bloc also important
    print('error is ',z)
    print("you can not divide by zero")
except : #without specifying any errortype #must be at the last
    print("this is default except block")
    